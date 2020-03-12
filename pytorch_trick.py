#find the version
import torch
print(torch.__version__)

#tensor declaration
image_tensor = torch.zeros([480, 640], dtype=torch.int32)

#image to 4D tensor
image_tensor = (torch.from_numpy(image).permute(2, 0, 1).contiguous()).unsqueeze(0)

#tensor to cuda tensor
tensor_gpu = Variable(tesnor_cpu).cuda(non_blocking=True)

#tensor to numpy
data = tensor_gpu.cpu().numpy()
#in case grad use
data = tensor_gpu.detach().cpu().numpy()

#load .pth
torch.load(*.pth)

