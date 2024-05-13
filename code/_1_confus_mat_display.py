"""
Filename: _1_confus_mat_display.py <br>
Title: Display the customized confusion matrix <br>
Author: Raghava | GitHub: @raghavtwenty <br>
Date Created: June 10, 2023 | Last Updated: May 13, 2024 <br>
Language: Python | Version: 3.10.14, 64-bit <br>
"""

# Importing required library
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


# Matrix display
def display_confus_matrix(actual, pred):
    confus_matrix = confusion_matrix(actual, pred)
    confus_matrix_dis = ConfusionMatrixDisplay(
        confusion_matrix=confus_matrix,
        display_labels=["Normal", "Blackhole", "TCP-SYN", "PortScan", "Diversion"],
    )
    confus_matrix_dis.plot()


# Main
if __name__ == "__main__":
    display_confus_matrix(y_test, y_pred_nb)
