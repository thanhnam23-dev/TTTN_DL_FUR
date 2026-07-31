import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from sklearn.metrics import roc_curve, precision_recall_curve, auc
from sklearn.preprocessing import label_binarize

LOGS_DIR = Path(r"S:\Thực tập tốt nghiệp\logs")
PLOTS_DIR = Path(r"S:\Thực tập tốt nghiệp\plots")
PLOTS_DIR.mkdir(parents=True, exist_ok=True)

MODELS = ["mobilenet_v2", "resnet18", "efficientnet_b0"]
MODEL_DISPLAY_NAMES = {
    "mobilenet_v2": "MobileNetV2",
    "resnet18": "ResNet18",
    "efficientnet_b0": "EfficientNet-B0"
}
COLORS = {
    "mobilenet_v2": "#2b5c8f",
    "resnet18": "#d9534f",
    "efficientnet_b0": "#27ae60"
}

def plot_learning_curves():
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    for m in MODELS:
        hist_file = LOGS_DIR / f"{m}_history.json"
        if not hist_file.exists():
            continue
        with open(hist_file, 'r', encoding='utf-8') as f:
            hist = json.load(f)

        epochs = range(1, len(hist["train_loss"]) + 1)
        name = MODEL_DISPLAY_NAMES[m]

        # Loss plot
        axes[0].plot(epochs, hist["val_loss"], label=f"{name} (Val)", color=COLORS[m], linewidth=2)
        axes[0].plot(epochs, hist["train_loss"], label=f"{name} (Train)", color=COLORS[m], linestyle='--', alpha=0.6)

        # Accuracy plot
        axes[1].plot(epochs, hist["val_acc"], label=f"{name} (Val)", color=COLORS[m], linewidth=2)
        axes[1].plot(epochs, hist["train_acc"], label=f"{name} (Train)", color=COLORS[m], linestyle='--', alpha=0.6)

    axes[0].set_title("Validation & Training Loss Comparison", fontsize=12, fontweight='bold')
    axes[0].set_xlabel("Epochs")
    axes[0].set_ylabel("Loss")
    axes[0].legend()
    axes[0].grid(True, linestyle=':', alpha=0.6)

    axes[1].set_title("Validation & Training Accuracy Comparison", fontsize=12, fontweight='bold')
    axes[1].set_xlabel("Epochs")
    axes[1].set_ylabel("Accuracy")
    axes[1].legend()
    axes[1].grid(True, linestyle=':', alpha=0.6)

    plt.tight_layout()
    out_path = PLOTS_DIR / "learning_curves.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[SAVED] Learning curves plot saved to: {out_path}")

def plot_confusion_matrices():
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    for idx, m in enumerate(MODELS):
        metrics_file = LOGS_DIR / f"{m}_metrics.json"
        if not metrics_file.exists():
            continue
        with open(metrics_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        cm = np.array(data["confusion_matrix"])
        class_names = data["class_names"]
        name = MODEL_DISPLAY_NAMES[m]

        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[idx],
                    xticklabels=class_names, yticklabels=class_names, cbar=False)
        axes[idx].set_title(f"Confusion Matrix - {name}", fontsize=12, fontweight='bold')
        axes[idx].set_xlabel("Predicted Label")
        axes[idx].set_ylabel("True Label")
        axes[idx].tick_params(axis='x', rotation=30)

    plt.tight_layout()
    out_path = PLOTS_DIR / "confusion_matrices.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[SAVED] Confusion matrices plot saved to: {out_path}")

def plot_roc_pr_curves():
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    for m in MODELS:
        metrics_file = LOGS_DIR / f"{m}_metrics.json"
        if not metrics_file.exists():
            continue
        with open(metrics_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        targets = np.array(data["targets"])
        probs = np.array(data["probabilities"])
        y_test_bin = label_binarize(targets, classes=list(range(len(data["class_names"]))))
        name = MODEL_DISPLAY_NAMES[m]

        # Weighted ROC curve
        fpr, tpr, _ = roc_curve(y_test_bin.ravel(), probs.ravel())
        roc_auc = auc(fpr, tpr)
        axes[0].plot(fpr, tpr, label=f"{name} (AUC = {roc_auc:.4f})", color=COLORS[m], linewidth=2)

        # Weighted PR curve
        precision, recall, _ = precision_recall_curve(y_test_bin.ravel(), probs.ravel())
        pr_auc = auc(recall, precision)
        axes[1].plot(recall, precision, label=f"{name} (PR-AUC = {pr_auc:.4f})", color=COLORS[m], linewidth=2)

    axes[0].plot([0, 1], [0, 1], 'k--', alpha=0.5)
    axes[0].set_title("ROC Curves Comparison", fontsize=12, fontweight='bold')
    axes[0].set_xlabel("False Positive Rate")
    axes[0].set_ylabel("True Positive Rate")
    axes[0].legend()
    axes[0].grid(True, linestyle=':', alpha=0.6)

    axes[1].set_title("Precision-Recall (PR) Curves Comparison", fontsize=12, fontweight='bold')
    axes[1].set_xlabel("Recall")
    axes[1].set_ylabel("Precision")
    axes[1].legend()
    axes[1].grid(True, linestyle=':', alpha=0.6)

    plt.tight_layout()
    out_path = PLOTS_DIR / "roc_pr_curves.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[SAVED] ROC and PR curves plot saved to: {out_path}")

def plot_metrics_comparison():
    csv_path = LOGS_DIR / "model_comparison.csv"
    if not csv_path.exists():
        return

    df = pd.read_csv(csv_path)
    df["Model"] = df["Model"].map(MODEL_DISPLAY_NAMES)

    df_melted = df.melt(id_vars=["Model"], var_name="Metric", value_name="Score")

    plt.figure(figsize=(10, 5))
    palette = {"MobileNetV2": COLORS["mobilenet_v2"], "ResNet18": COLORS["resnet18"], "EfficientNet-B0": COLORS["efficientnet_b0"]}

    ax = sns.barplot(data=df_melted, x="Metric", y="Score", hue="Model", palette=palette)
    plt.title("Model Performance Metrics Comparison", fontsize=14, fontweight='bold')
    plt.ylim(0.80, 1.02)
    plt.ylabel("Score")
    plt.grid(axis='y', linestyle=':', alpha=0.6)

    for p in ax.patches:
        height = p.get_height()
        if height > 0:
            ax.annotate(f"{height:.3f}",
                        (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='bottom', fontsize=8, xytext=(0, 2),
                        textcoords='offset points')

    plt.tight_layout()
    out_path = PLOTS_DIR / "metrics_comparison_barchart.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[SAVED] Metrics comparison bar chart saved to: {out_path}")

def main():
    print("=== Generating Plot Graphics for Report & Dashboard ===")
    plot_learning_curves()
    plot_confusion_matrices()
    plot_roc_pr_curves()
    plot_metrics_comparison()
    print("=== PLOTTING COMPLETED ===")

if __name__ == "__main__":
    main()
