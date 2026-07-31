import os
import shutil
import random
from pathlib import Path

# Thư mục gốc chứa data thô và thư mục đích
RAW_DATA_DIR = Path(r"S:\Thực tập tốt nghiệp\data")
OUTPUT_DIR = Path(r"S:\Thực tập tốt nghiệp\dataset")

CLASS_MAPPING = {
    "Bar Stool Dataset": "bar_stool",
    "Bed Dataset": "bed",
    "Chair Dataset": "chair",
    "Coffee Table Dataset": "coffee_table",
    "Dinning Table DataSet": "dining_table",
    "Dresser Dataset": "dresser"
}

VALID_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

def process_dataset(train_ratio=0.70, val_ratio=0.15, test_ratio=0.15, seed=42):
    random.seed(seed)
    
    print("=== Start Processing Dataset ===")
    
    summary = {}
    
    for raw_folder, class_name in CLASS_MAPPING.items():
        class_raw_path = RAW_DATA_DIR / raw_folder
        if not class_raw_path.exists():
            print(f"[WARNING] Folder not found: {raw_folder}")
            continue
            
        image_files = []
        for root, _, files in os.walk(class_raw_path):
            for file in files:
                ext = Path(file).suffix.lower()
                if ext in VALID_EXTS:
                    image_files.append(Path(root) / file)
                    
        print(f"-> Class '{class_name}': Found {len(image_files)} images.")
        
        random.shuffle(image_files)
        
        total = len(image_files)
        n_train = int(total * train_ratio)
        n_val = int(total * val_ratio)
        n_test = total - n_train - n_val
        
        splits = {
            "train": image_files[:n_train],
            "val": image_files[n_train:n_train + n_val],
            "test": image_files[n_train + n_val:]
        }
        
        summary[class_name] = {
            "total": total,
            "train": len(splits["train"]),
            "val": len(splits["val"]),
            "test": len(splits["test"])
        }
        
        for split_name, files in splits.items():
            split_class_dir = OUTPUT_DIR / split_name / class_name
            split_class_dir.mkdir(parents=True, exist_ok=True)
            
            for idx, src_path in enumerate(files, start=1):
                ext = src_path.suffix.lower()
                dest_filename = f"{class_name}_{idx:04d}{ext}"
                dest_path = split_class_dir / dest_filename
                shutil.copy2(src_path, dest_path)

    print("\n=== DATASET PROCESSING COMPLETE ===")
    print(f"{'Class':<15} | {'Total':<7} | {'Train':<7} | {'Val':<7} | {'Test':<7}")
    print("-" * 55)
    for cls, counts in summary.items():
        print(f"{cls:<15} | {counts['total']:<7} | {counts['train']:<7} | {counts['val']:<7} | {counts['test']:<7}")
    print("-" * 55)
    
if __name__ == "__main__":
    process_dataset()
