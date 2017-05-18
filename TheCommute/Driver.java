import java.awt.*;


public class Driver extends GameApplet
{
	public static int SCREEN_WIDTH = 800;
	public static int SCREEN_HEIGHT = 600;
	
	public static int halfWidth = SCREEN_WIDTH / 2;
	public static int halfHeight = SCREEN_HEIGHT / 2;
	
	Car Jumba;
	Car Pedestrian[] = new Car[10];
	BackgroundManager BM;
	
	public void initialize()
	{
		setDuration(20);
		Jumba = new Car(halfWidth - 25, halfHeight + halfHeight / 2 - 46, 50, 92, "Images/Cars/JumbaTiny", 0);
		BM = new BackgroundManager("Images/Tiles/grass", "Images/Tiles/concrete", "Images/Tiles/concreteWhiteLine");
	}   
	
	public void respondToInput()
	{
		// Go, stop, or coast
		if(input[_W])
		{
			Jumba.Accelerate();
		}
		else if(input[_S])
		{
			Jumba.Decelerate();
		}
		else
		{
			Jumba.Coast();
		}
		
		// Turn
		if(input[_A])
		{
			Jumba.TurnLeft();
		}
		if(input[_D])
		{
			Jumba.TurnRight();
		}
		
		// Change Gears
		if(input[UP])
		{
			Jumba.ShiftUp();
			upPressed = false;
			input[UP] = false;
		}
		if(input[DN])
		{
			Jumba.ShiftDown();
			downPressed = false;
			input[DN] = false;
		}
	}
	
	public void moveGameObjects()
	{
		Camera2D.moveUpBy(Jumba.getSpeed());
	}
	
	public void handleCollisions()
	{
		
	}
	
	public void paint(Graphics g)
	{
		BM.draw(g);
		Jumba.draw(g);
		g.drawString("Speed:"+(Jumba.getSpeed() + " Gear:" + Jumba.getGear()), 25, 25);
	}
}
