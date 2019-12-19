class TrackableObject:
	def __init__(self, objectID, centroid):
		# store the object ID, then initialize a list of centroids
		# using the current centroid
		self.objectID = objectID
		self.centroids = [centroid]

		# initialize a boolean used to indicate if the object has
		# already been counted or not
		self.counted = False


# Tạo một đối tượng có thể theo dõi được
# Để theo dõi và đếm một đối tượng trong luồng video, chúng ta cần một cách dễ dàng để lưu trữ thông tin liên quan đến chính đối tượng đó, bao gồm:

# Đó là ID đối tượng
# Đó là các trọng tâm trước đó (vì vậy chúng ta có thể dễ dàng tính toán hướng di chuyển của vật thể)
# Có hay không đối tượng đã được tính

# Hàm tạo TrackableObject chấp nhận một objectID + centroid và lưu trữ chúng. Biến centroids là một danh sách vì nó sẽ chứa một lịch sử vị trí trung tâm.
# Hàm tạo cũng khởi tạo được tính là Sai, cho biết đối tượng chưa được tính.
# https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/?fbclid=IwAR0FDh90OLstH116UElfdvoDLnXzxb6o_aOv4rMiCQmohjaL0apIeBw3rAg