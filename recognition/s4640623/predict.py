import torch
import torch.nn.functional as func

import train
import dataset
import modules

"""Test model functionality with test dataset"""
def test(model, adj, features, target):
    model.eval()
    output = model(features, adj)
    # Use test dataset indicies to calculate loss and accuracy
    loss_test = func.nll_loss(output[test_ds], target[test_ds])
    acc_test = accuracy(output[test_ds], target[test_ds])
    print("loss= {:.4f}".format(loss_test.item()),
          "accuracy= {:.4f}".format(acc_test.item()))

# Load variables for testing
data = load_data()
train_ds, valid_ds, test_ds, features, target, edges = process_data(dataset)
model = model_init(features, data)
adj = adj_matrix(data)
test(model, adj, features, target)
