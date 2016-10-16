public struct Student
{
    public string id;
    public int[] pos = new int[4];
    public double emotions = new double[8];
    public Person(string id, int pos, double emotions)
    {
        ID = id;
        position = pos;
	Emo = emotions;
    }
}

public class Application
{
    static void Main(JSONRetVal)
    {
        // Create  struct instance and initialize by using "new".
        // Memory is allocated on thread stack.

        Student s1 = new Student("", int [4], double [8]);

        s1.ID = 12345;
        s1.position[0] = JSONRetVal[0]["left"]
	s1.position[1] = JSONRetVal[0]["top"]
	s1.position[2] = JSONRetVal[0]["width"]
	s1.position[3] = JSONRetVal[0]["height"]
	
	s1.EMo[0] = JSONRetVal[1]["anger"]
	s1.EMo[0] = JSONRetVal[1]["contempt"]
	s1.EMo[0] = JSONRetVal[1]["disgust"]
	s1.EMo[0] = JSONRetVal[1]["fear"]
	s1.EMo[0] = JSONRetVal[1]["happiness"]
	s1.EMo[0] = JSONRetVal[1]["neutral"]
	s1.EMo[0] = JSONRetVal[1]["sadness"]
	s1.EMo[0] = JSONRetVal[1]["surprise"]
    }
}
