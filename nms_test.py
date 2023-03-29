#输出shape:（batch_size,all_boxes,4+1+num_classes）
#            1         num_boxes,xyhw+obj+num_classes
import numpy as np

#TODO:输入的是两个不同模型的boxes输出
#TODO：两个模型boxes经过NMS的输出变量为pred，格式为（all_boxes,4+1+num_classes），即没有batchsize维度
#TODO：粗粒度模型num_classes为1，即4+1+1；细粒度模型num_classes为n，即4+1+n；
#TODO:NMS应该接收两个boxes变量，一个coarse_grained_boxes，一个fine_grained_boxes
#TODO:输出应该既有粗粒度的box，又有细粒度的box
#TODO：框形式转换，conf_thres、nms_thres流程对两种box处理相同
#TODO:细粒度boxes是一个list：finebox_list，粗粒度boxes是另一个list:coarsebox_list;
#TODO：创建一个返回最终结果的list：res_list;

#TODO:不需要区分类别，每次从finebox_list中拿出一个box，与coarsebox_list进行逐个比对，去除coarsebox_list中大于iou的box。

#hard-nms for FineAndCoarse，没有多余的操作
#该函数只能减少漏检，无法抑制误检的出现
def NMS_for_FineAndCoarse(boxes_fine,boxes_coarse,nms_thres=0.4):
    #output[0]:fine_boxes   output[1]:coarse_boxes
    output=[]
    res_box=[]
    while len(boxes_fine)!=0:
        res_box.append(boxes_fine[0])
        ious=iou(res_box[-1],boxes_coarse[:])
        boxes_coarse=boxes_coarse[:][ious<0.4]
        boxes_fine=boxes_fine[1:]
    output.append(res_box)
    output.append(boxes_coarse)
    return output

#TODO:mergeNMS or WBF的实现
#TODO：
def mergeNMS_for_FineAndCoarse(boxes_fine,boxes_coarse,nms_thres=0.4):
    #output[0]:fine_boxes   output[1]:coarse_boxes
    output=[]
    res_box=[]
    while len(boxes_fine)!=0:
        res_box.append(boxes_fine[0])
        ious=iou(res_box[-1],boxes_coarse[:])
        boxes_coarse=boxes_coarse[:][ious<0.4]
        boxes_fine=boxes_fine[1:]
    output.append(res_box)
    output.append(boxes_coarse)
    return output

def non_max_suppression(boxes,num_classes,conf_thres=0.5,nms_thres=0.4):
    bs=np.shape(boxes)[0]
    #转换框的形式，转换为左下角、右上角的形式。
    shape_boxes=np.zeros_like(boxes[:,:,:4])
    shape_boxes[:,:,0]=boxes[:,:,0]-boxes[:,:,2]/2
    shape_boxes[:,:,1]=boxes[:,:,1]-boxes[:,:,3]/2
    shape_boxes[:,:,2]=boxes[:,:,0]+boxes[:,:,2]/2
    shape_boxes[:,:,3]=boxes[:,:,1]+boxes[:,:,3]/2

    boxes[:,:,:4]=shape_boxes

    output=[]

    for i in range(bs):
        #predictionShape:(num_boxes,leftx+lefty+rightx+righty+obj+num_classes)
        prediction=boxes[i]
        score=prediction[:,4]
        mask=score>conf_thres
        detections=prediction[mask]
        #最大类别置信度
        class_conf=np.expend_dims(np.max(detections[:,5:],axis=-1),axis=-1)
        #最大类别置信度的索引
        class_pred=np.expend_dims(np.argmax(detections[:,5:],axis=-1),axis=-1)
        #detections shape:(num_boxes,leftx+lefty+rightx+righty+obj+conf+pred)
        detections=np.concatenate([detections[:,:5],class_conf,class_pred],-1)

        unique_class=np.unique(detections[:,-1])
        if len(unique_class)==0:
            continue
        best_box=[]
        for c in unique_class:
            cls_mask=detections[:,-1]==c

            #筛选出detections中属于同一类别c的部分
            detection=detections[cls_mask]

            #根据obj置信度由高到低排序
            scores=detection[:,4]
            arg_sort=np.argsort(scores)[::-1]
            detection=detection[arg_sort]

            #取最大置信度候选框，与其他的计算iou
            while len(detection)!=0:
                best_box.append(detection[0])
                if len(detection) ==1:
                    break
                ious=iou(best_box[-1],detection[1:])
                detection=detection[1:][ious<nms_thres]
        output.append(best_box)
    return np.array(output)

def iou(b1,b2):
    b1_x1,b1_y1,b1_x2,b1_y2=b1[0],b1[1],b1[2],b1[3]
    b2_x1,b2_y1,b2_x2,b2_y2=b2[:,0],b2[:,1],b2[:,2],b2[:,3]

    inter_rect_x1=np.maximum(b1_x1,b2_x1)
    inter_rect_y1=np.maximum(b1_y1,b2_y1)
    inter_rect_x2=np.maximum(b1_x2,b2_x2)
    inter_rect_y2=np.maximum(b1_y2,b2_y2)

    inter_area=np.maximum(inter_rect_x2-inter_rect_x1,0)* \
               np.maximum(inter_rect_y2-inter_rect_y1,0)

    area_b1=(b1_x2-b1_x1)*(b1_y2-b1_y1)
    area_b2=(b2_x2-b2_x1)*(b2_y2-b2_y1)

    iou=inter_area/np.maximum((area_b1+area_b2-inter_area),1e-6)
    return iou