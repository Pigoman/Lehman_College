import java.awt.*;

public class Car extends Sprite
{
	private int speed;
	private int gear;
	private int pause;
	private int speedLimit;
	private int countdown;
	private int speedWaiver;
	private int coastCount;
	private boolean shiftLight;
	private static String[] toSuper = new String[] {"UP"};
	
	//double x, double y,int w, int h, String filename, int count, int duration, String[] action
	public Car(double x, double y, int w, int h, String filename, int speedLimit)
	{
		super(x, y, w, h, filename, 1, 1, toSuper);
		ResetCar();
		this.speedLimit = speedLimit;
	}
	
	public void AIDrive()
	{
		// Give AI to other cars
		// Add random factor for speeding
		if(countdown == 0)
		{
			speedWaiver = (int)(Math.random() * 10 - 5);
			countdown = 100;
		}
		else
		{
			countdown--;
		}
		if(speed < speedLimit + speedWaiver)
		{
			Accelerate();
			if(shiftLight)
				ShiftUp();
		}
	}
	
	public void SetSpeedLimit(int newLimit)
	{
		speedLimit = newLimit;
	}
	
	public int getSpeed()
	{
		return speed;
	}
	
	public int getGear()
	{
		return gear;
	}
	
	public void ResetCar()
	{
		speed = 0;
		gear = 1;
		pause = 0;
		countdown = 100;
		speedWaiver = (int)(Math.random() * 10 - 5);
		coastCount = 50;
		shiftLight = false;
	}
	
	public void Accelerate()
	{
		// Accelerates at different rates to different top speeds in different gears
		if(pause == 0)
		{
			switch(gear)
			{
				case 1:
					if(speed < 5)
					{
						speed += 1;
					}
					else if(speed < 10)
					{
						speed += 2;
					}
					else if(speed < 15)
					{
						if(!shiftLight)
							shiftLight = true;
						speed += 3;
					}
					else if(speed < 20)
					{
						if(!shiftLight)
							shiftLight = true;
						speed -= 1;
					}
					else
					{
						speed -= 10;
					}
					break;
				case 2:
					if(speed < 20)
					{
						speed += 1;
					}
					else if(speed < 30)
					{
						if(!shiftLight)
							shiftLight = true;
						speed += 2;
					}
					else if(speed < 60)
					{
						if(!shiftLight)
							shiftLight = true;
						speed += 3;
					}
					else if(speed < 65)
					{
						if(!shiftLight)
							shiftLight = true;
						speed -= 2;
					}
					else
					{
						speed -= 5;
					}
					break;
				case 3:
					if(speed < 25)
					{
						speed += 1;
					}
					else if(speed < 45)
					{
						if(!shiftLight)
							shiftLight = true;
						speed += 2;
					}
					else if(speed < 75)
					{
						speed += 3;
					}
					else
					{
						speed -= 3;
					}
					break;
				case 4:
					if(speed < 30)
					{
						speed += 1;
					}
					else if(speed < 50)
					{
						if(!shiftLight)
							shiftLight = true;
						speed += 2;
					}
					else if(speed < 90)
					{
						speed += 3;
					}
					else
					{
						speed -= 3;
					}
					break;
				case 5:
					if(speed < 45)
					{
						speed += 1;
					}
					else if(speed < 65)
					{
						if(!shiftLight)
							shiftLight = true;
						speed += 2;
					}
					else if(speed < 120)
					{
						speed += 3;
					}
					else
					{
						speed -= 3;
					}
					break;
				default:
					gear = 1;
					speed = 0;
					break;
			}
			pause = 5;
		}
		else
		{
			pause--;
		}
	}
	
	public void Decelerate()
	{
		// Decelerates as if the driver is braking and engine braking
		if(pause == 0)
		{
			switch(gear)
			{
				case 1:
					if(speed < 5 && speed > 0)
					{
						speed -= 1;
					}
					else if(speed < 10 && speed > 0)
					{
						speed -= 2;
					}
					else if(speed < 15 && speed > 0)
					{
						speed -= 3;
					}
					else
					{
						speed -= 10;
					}
					break;
				case 2:
					if(speed < 20 && speed > 0)
					{
						speed -= 1;
					}
					else if(speed < 30 && speed > 0)
					{
						speed -= 2;
					}
					else if(speed < 60 && speed > 0)
					{
						speed -= 3;
					}
					else
					{
						speed -= 7;
					}
					break;
				case 3:
					if(speed < 25 && speed > 0)
					{
						speed -= 1;
					}
					else if(speed < 45 && speed > 0)
					{
						speed -= 2;
					}
					else if(speed < 75 && speed > 0)
					{
						speed -= 3;
					}
					else
					{
						speed -= 5;
					}
					break;
				case 4:
					if(speed < 30 && speed > 0)
					{
						speed -= 1;
					}
					else if(speed < 50 && speed > 0)
					{
						speed -= 2;
					}
					else if(speed < 90 && speed > 0)
					{
						speed -= 3;
					}
					else
					{
						speed -= 5;
					}
					break;
				case 5:
					if(speed < 45 && speed > 0)
					{
						speed -= 1;
					}
					else if(speed < 65 && speed > 0)
					{
						speed -= 2;
					}
					else if(speed < 120 && speed > 0)
					{
						speed -= 3;
					}
					else
					{
						speed -= 5;
					}
					break;
				default:
					gear = 1;
					speed = 0;
					break;
			}
			if(speed <= 0)
			{
				speed = 0;
			}
			pause = 10;
		}
		else
		{
			pause--;
		}
	}
	
	public void Coast()
	{
		if(speed > 0 && coastCount == 0)
		{
			speed--;
			coastCount = 50;
		}
		else
		{
			if(coastCount > 0)
			{
				coastCount--;
			}
			//System.out.println("Coast Count: " + coastCount);
		}
	}
	
	public void TurnLeft()
	{
		if(x > 0 && speed > 0)
			x--;
	}
	
	public void TurnRight()
	{
		if(x < Driver.SCREEN_WIDTH - w & speed > 0)
			x++;
	}
	
	public void ShiftUp()
	{
		if(gear < 5)
		{
			gear++;
			pause = 20;
			shiftLight = false;
		}
	}
	
	public void ShiftDown()
	{
		if(gear > 1)
		{
			gear--;
			pause = 20;
		}
	}
}
