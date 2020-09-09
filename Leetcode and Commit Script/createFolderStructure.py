import os

path = "D:\\Personal\\Leetcode"
problemName = """1450. Number of Students Doing Homework at a Given Time"""

problemName = problemName.replace("\n", "")
problemName = problemName.lstrip(" ")
problemName = problemName.rstrip(" ")

problemNumber = "P"+str(problemName.split(".")[0])
problemName = problemName.split(".")[1].replace(" ","_")

fullProblemName = problemNumber + problemName
folderPath = os.path.join(path,fullProblemName)

os.mkdir(folderPath)
filePath = os.path.join(folderPath,fullProblemName+".java")
file = open(filePath,"w")
file.write("""class Solution {
    public int runningSum() {
        
        return 0;
    }
	public static void main(String[] args) {
        Solution sol = new Solution();
        int result = sol.runningSum();
        System.out.println(result);
    }
}""")
file.close()

htmlfilePath = os.path.join(folderPath,"Problem.html")
file = open(htmlfilePath, "w")
file.write("""<html>
<head></head>
<body>

</body>
</html>
""")
file.close()

os.system("code "+filePath)
print(fullProblemName)