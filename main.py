class Package:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    
class SAMPLE:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

class Layer:
    def __init__(self, num_samples, sample_length, sample_width, sample_height):
        self.num_samples = num_samples
        self.sample_length = sample_length
        self.sample_width = sample_width
        self.sample_height = sample_height
        self.calculate_dimensions()

    def calculate_dimensions(self):
        self.length = 2 * self.sample_length
        self.width = self.sample_width
        self.height = ((self.num_samples + 1) // 2) * self.sample_height

def main():
    SmallBox = Package(25.5, 33, 6)
    LargeBox = Package(25.5, 33, 12)
    
    num_samples = int(input("Enter the number of samples: "))
    samples = []
    for _ in range(num_samples):
        samples.append(SAMPLE(12, 29.5, 2.2))
    
    if num_samples >= 1:
        layer = Layer(num_samples, 12, 29.5, 2.2)
        print(f"Layer dimensions: Length={layer.length}, Width={layer.width}, Height={layer.height}")
        
        if layer.length < SmallBox.length and layer.width < SmallBox.width and layer.height < SmallBox.height and num_samples <= 4:
            print("All samples fit in SmallBox")
        elif layer.length < LargeBox.length and layer.width < LargeBox.width and layer.height < LargeBox.height and num_samples <= 8:
            print("All samples fit in LargeBox")
        else:
            SmallBox_count = 0
            LargeBox_count = 0
            remaining_samples = num_samples
            
            while remaining_samples > 0:
                if remaining_samples <= 4:
                    SmallBox_count += 1
                    remaining_samples -= 4
                elif remaining_samples <= 8:
                    LargeBox_count += 1
                    remaining_samples -= 8
                else:
                    LargeBox_count += 1
                    remaining_samples -= 8
            
            print(f"Need {SmallBox_count} x SmallBox and {LargeBox_count} x LargeBox to fit all the samples")
    else:
        print("Not enough samples to form a layer")

if __name__ == "__main__":
    main()