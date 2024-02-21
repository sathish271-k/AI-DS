class multiplefunction():



    def Subfields():
        subfields = [
            "Sub-fields in AI are:",
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]
        for field in subfields:
            print(field)
        
    

    def oddEven():
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"{num} is an even number.")
        else:
            print(f"{num} is an odd number.")
            
            
            
    def Elegible():
        gender = input("Your Gender: ")
        age = int(input("Your Age: "))

        gender = gender.upper()
        if gender == 'MALE' and age >= 21:
            return "ELIGIBLE"
        elif gender == 'FEMALE' and age >= 18:
            return "ELIGIBLE"
        else:
            return "NOT ELIGIBLE"

        print(Elegible())
        
        
        
    def percentage():
        
        marks = [] 
        
        for i in range(1, 6):
            mark = int(input(f"Subject{i} = "))
            marks.append(mark)

        total = sum(marks)  
        percentage = (total / (5 * 100)) * 100
        print(f"Total: {total}") 
        print(f"Percentage: {percentage:.14f}%")
        
        
        
    def triangle():
        a = float(input('Height: '))
        b = float(input('Breadth: '))

        area = (a * b) / 2
        print("Area formula: (Height*Breadth)/2")
        print(f'Area of Triangle: {area:.2f}')

        c = float(input('Height1: '))
        d = float(input('Height2: '))
        e = float(input('Breadth: '))

        perimeter = c + d + e
        print("Perimeter formula: Height1+Height2+Breadth")
        print(f'Perimeter of Triangle: {perimeter:.2f}')
