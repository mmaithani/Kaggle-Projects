# single box plotting
def plot():
    color = (0,0,255) 
    thickness = 2
    xmax =xmin+width
    ymax =ymin+height
    
    img = cv2.imread(train_dir+image_id+'.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img= cv2.rectangle(img,(xmin,ymin), (xmax,ymax),color,thickness)

    plt.figure(figsize=(20, 20))
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    
def get_bbox(image_id):
    df=train.where(train['image_id']== image_id)
    df =df.dropna(axis='rows')
    arr = df["bbox"].to_numpy()
    return(arr)

def show_box(image_id):
    df=train.where(train['image_id']== image_id)
    df =df.dropna(axis='rows')
    arr = df["bbox"].to_numpy()

    img = cv2.imread(train_dir+image_id+'.jpg')
    # opencv always read image as BGR - conversion is must
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    for box in arr:
        box=box[1:-1]
        xmin,ymin,width,height= box.split(",")
        # converting string to int
        xmin= int(float(xmin)); ymin= int(float(ymin)) 
        width= int(float(width)) ; height= int(float(height))

        xmax =xmin+width
        ymax =ymin+height

        img= cv2.rectangle(img,(xmin,ymin), (xmax,ymax),(255,0,0),2)
        
        img1 = Image.fromarray(img) # cv2 to PIL
    return img1
#     plt.figure(figsize=(20, 20))
#     plt.subplot(1, 2, 1)
#     plt.imshow(img1)
