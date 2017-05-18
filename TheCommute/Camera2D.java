public class Camera2D
{
	static double x;
	static double y;
	
	public static void moveUpBy(int dy)
	{
		y -= dy;
	}
	
	public static void moveDnBy(int dy)
	{
		y += dy;
	}
	
	public static void moveLtBy(int dx)
	{
		x -= dx;
	}
	
	public static void moveRtBy(int dx)
	{
		x += dx;
	}
}
