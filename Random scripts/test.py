from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt

y_true = [1, 1, 0, 1, 1, 1, 0]
y_pred = [0.14, 0.15, 0.27, 0.61, 0.71, 0.75, 0.81]
fpr, tpr, thresholds = metrics.roc_curve(y_true, y_pred, pos_label=0)

# Print ROC curve
plt.plot(fpr,tpr)
plt.show()

# Print AUC
auc = np.trapz(tpr,fpr)
print('AUC:', auc)