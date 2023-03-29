import cv2
import os
def save_img(dirspath):
    videodir_names = os.listdir(dirspath)

    for videodir in videodir_names:

        videos=os.listdir(os.path.join(dirspath,videodir))
        frame_save_dir=os.path.join(dirspath,videodir+'_frames')
        if not os.path.exists(frame_save_dir):
            os.makedirs(frame_save_dir)
        for video in videos:
            video_path=os.path.join(dirspath,videodir)
            video_name=video.split('.')[0]
            vc=cv2.VideoCapture(video_path+'/'+video)
            c=0
            rval=vc.isOpened()
            print(str(rval))
            while rval:
                c=c+1
                rval,frame=vc.read()
                frame_save_path=frame_save_dir+'/'+video_name+str(c)+'.jpg'
                if rval:
                    if videodir=='1s':
                        if c<=20 and c%2==0:
                            cv2.imwrite(frame_save_path, frame)
                            cv2.waitKey(1)
                    else:
                        if c%20==0:
                            cv2.imwrite(frame_save_path, frame)
                            cv2.waitKey(1)
                    # elif c%10==0:
                    #     cv2.imwrite(frame_save_path,frame)
                    #     cv2.waitKey(1)
                else:
                    break
            vc.release()
            print('save_success')
            print(video_name)

dirspath='/home/nrz/下载/鱼道垃圾视频'
save_img(dirspath)