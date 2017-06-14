import java.awt.*;


public class Driver extends GameApplet
{
	public static int SCREEN_WIDTH = 800;
	public static int SCREEN_HEIGHT = 600;
	
	public static int halfWidth = SCREEN_WIDTH / 2;
	public static int halfHeight = SCREEN_HEIGHT / 2;
	
	public static int SCORE;
	
	// The Player
	Car Jumba;
	// AI Cars
	Car Pedestrian[] = new Car[12];
	// Moves the background tiles so they always sho wup on the screen
	BackgroundManager BM;
	
	public void initialize()
	{
		// Set better delay between frames for smoother game
		setDuration(20);
		
		SCORE = 0;
		
		String PedFileName;
		
		Jumba = new Car(halfWidth - 25, halfHeight + halfHeight / 2, 50, 92, "Images/Cars/Jumba", 0, true);
		for(int i = 0; i < Pedestrian.length; i++)
		{
			//public Car(double x, double y, int w, int h, String filename, int speedLimit)
			if(i % 3 == 0)
				PedFileName = "Images/Cars/Beetle";
			else
				PedFileName = "Images/Cars/Corolla";
			Pedestrian[i] = new Car(halfWidth - 75 + 100 * (i % 4 - 1), (-92) - 1000 * (i / 4), 50, 92, PedFileName, 45, false);
		}
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
		// Keep Score
		SCORE = (int)Math.abs(Camera2D.y);
		
		// Check to make sure Player hasn't died
		Jumba.IsAlive();
		
		// Move the ground under the player
		Camera2D.moveUpBy(Jumba.getSpeed());
		
		// Move the AI cars in relation to the player's speed
		for(int i = 0; i < Pedestrian.length; i++)
		{
			Pedestrian[i].AIDrive();
			Pedestrian[i].y += Jumba.getSpeed() - Pedestrian[i].getSpeed();
			if(Pedestrian[i].y < Camera2D.y - 4000)
			{
				Pedestrian[i].y += 1000 + Math.random() * 100;
				//System.out.println("Pedestrian["+i+"] got too far. Pulling back...");
			}
			if(Pedestrian[i].y > 3000)
			{
				Pedestrian[i].y -= 6000 + Math.random() * 100;
				//System.out.println("Adjusted Pedestrian["+i+"]");
			}
		}
	}
	
	public void handleCollisions()
	{
		// If the player runs off the road into the grass
		if(Jumba.x < 190 || Jumba.x > 610 - Jumba.w)
		{
			//System.out.println("On Grass");
			Jumba.OnGrass();
		}
		for(int i = 0; i < Pedestrian.length; i++)
		{
			if(Jumba.hasCollidedWith(Pedestrian[i]) && Jumba.getHealth() > 0)
			{
				//System.out.println("Collided with Pedestrian["+i+"]");
				int pedSpeed = Pedestrian[i].getSpeed();
				int JumSpeed = Jumba.getSpeed();
				Jumba.Collide(pedSpeed, Pedestrian[i].x, Pedestrian[i].y);
				Pedestrian[i].Collide(JumSpeed, Jumba.x, Jumba.y);
			}
			for(int j = 0; j < Pedestrian.length; j++)
			{
				if(j != i)
				{
					if(Pedestrian[i].hasCollidedWith(Pedestrian[j]))
					{
						//System.out.println("Pedestrian["+i+"] has collided with Pedestrian["+j+"]");
						int pedSpeedI = Pedestrian[i].getSpeed();
						int pedSpeedJ = Pedestrian[j].getSpeed();
						if(Pedestrian[i].y > Pedestrian[j].y)
						{
							Pedestrian[i].y += 5;
							Pedestrian[j].y -= 5;
						}
						else
						{
							Pedestrian[i].y -= 5;
							Pedestrian[j].y += 5;
						}
						Pedestrian[j].Collide(pedSpeedI, Pedestrian[i].x, Pedestrian[i].y);
						Pedestrian[i].Collide(pedSpeedJ, Pedestrian[j].x, Pedestrian[j].y);
					}
				}
			}
		}
	}
	
	public void paint(Graphics g)
	{
		g.setFont(new Font(Font.MONOSPACED, Font.BOLD, 16));
		BM.draw(g);
		for(int i = 0; i < Pedestrian.length; i++)
		{
			Pedestrian[i].draw(g);
			//g.drawString("Ped["+i+"]", (int)Pedestrian[i].x, (int)Pedestrian[i].y );
			//g.drawString(""+Pedestrian[i].getSpeed()+" "+Pedestrian[i].getGear(), (int)Pedestrian[i].x, (int)Pedestrian[i].y);
		}
		Jumba.draw(g);
		g.drawString("Health: " + Jumba.getHealth(), 0, 28);
		//g.drawString("Bang: " + Jumba.getRevBang(), 0, 56);
		g.drawString("Score: " + SCORE, 600, 28);
		if(Jumba.getSpeed() < 10)
			g.drawString("Speed: "+(Jumba.getSpeed() + "   Gear: " + Jumba.getGear()), 0, SCREEN_HEIGHT - 12);
		else if(Jumba.getSpeed() < 100)
			g.drawString("Speed: "+(Jumba.getSpeed() + "  Gear: " + Jumba.getGear()), 0, SCREEN_HEIGHT - 12);
		else
			g.drawString("Speed: "+(Jumba.getSpeed() + " Gear: " + Jumba.getGear()), 0, SCREEN_HEIGHT - 12);
		if(Jumba.getHealth() == 0)
		{
			g.setFont(new Font(Font.MONOSPACED, Font.BOLD, 64));
			g.drawString("GAME OVER", SCREEN_WIDTH / 2 - 175, SCREEN_HEIGHT / 2);
		}
	}
}
