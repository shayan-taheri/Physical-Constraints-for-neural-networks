import matplotlib.pyplot as plt
from src.vis_utils import visualize_grid

def save_net_weights(net, ids, name):
    ext = '.png'
    W1 = net.params['W1'][:,ids]
    W1 = W1.reshape(3, 32, 32, -1).transpose(3, 1, 2, 0)
    plt.imshow(visualize_grid(W1, padding=3).astype('uint8'))
    plt.gca().axis('off')
    plt.savefig('outputs/'+name+ext, dpi=300)
    plt.clf()
    #plt.savefig('')
    return None

def plot_train_loss(solver1, plot_name):
    plt.subplot(2, 1, 1)
    plt.title('Training loss')
    plt.plot(solver1.loss_history, 'o')
    plt.xlabel('Iteration')

    plt.subplot(2, 1, 2)
    plt.title('Accuracy')
    plt.plot(solver1.train_acc_history, '-o', label='train')
    plt.plot(solver1.val_acc_history, '-o', label='val')
    plt.plot([0.5] * len(solver1.val_acc_history), 'k--')
    plt.xlabel('Epoch')
    plt.legend(loc='lower right')
    plt.gcf().set_size_inches(15, 12)
    plt.savefig('outputs/'+plot_name+'.png')
    plt.clf()
    return None