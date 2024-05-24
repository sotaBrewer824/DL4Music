import torch
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
class MusicDataset(Dataset):
    def __init__(self, data, seq_len):
        super().__init__()
        self.data = data
        self.seq_len = seq_len

    def __getitem__(self, index):

        full_seq = torch.Tensor(self.data[index][:self.seq_len+1]).long()

        return full_seq.cuda()

    def __len__(self, BATCH_SIZE):
        return (len(self.data) // BATCH_SIZE) * BATCH_SIZE