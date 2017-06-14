import java.awt.*;

public class Car extends Sprite
{
	private int speed;
	private int gear;
	private int health;
	private int totalHealth;
	private int pause;
	private int speedLimit;
	private int countdown;
	private int speedWaiver;
	private int coastCount;
	private int grassCount;
	private int grassHealthCount;
	private int revBang;
	private int bangCount;
	private int boomCount;
	private boolean shiftLight;
	private boolean amPlayer;
	private boolean exploded;
	private static String[] toSuper = new String[] {"UP"};
	
	private Animation boom;
	
	private Audio crash;
	private Audio explode;
	private Audio idle;
	private Audio bang;
	
	//double x, double y,int w, int h, String filename, int count, int duration, String[] action
	public Car(double x, double y, int w, int h, String filename, int speedLimit, boolean amPlayer)
	{
		super(x, y, w, h, filename, 1, 1, toSuper);
		ResetCar();
		this.speedLimit = speedLimit;
		this.amPlayer = amPlayer;
		if(amPlayer)
		{
			boom = new Animation("Images/Explosion/explosion_UP_", 23, 5);
			crash = new Audio("Audio/Smash.wav");
			explode = new Audio("Audio/Explosion.wav");
			idle = new Audio("Audio/TurboEngineIdle.wav");
			bang = new Audio("Audio/Bang.wav");
		}
	}
	
	public void IsAlive()
	{
		totalHealth = health - revBang;
		if(totalHealth <= 0)
		{
			speed = 0;
			health = 0;
			revBang = 0;
			totalHealth = 0;
		}
		else
		{
			// Play engine noise if alive
			// Needs variation of pitch
			//idle.playLoop();
		}
	}
	
	public void AIDrive()
	{
		// Give AI to other cars
		// Add random factor for speeding
		if(countdown == 0)
		{
			speedWaiver = (int)(Math.random() * 10 - 5);
			countdown = 1000;
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
		else if(speed > speedLimit + speedWaiver + 5)
		{
			Decelerate();
		}
		else
		{
			Coast();
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
	
	public int getHealth()
	{
		return totalHealth;
	}
	
	public int getSpeedWaiver()
	{
		return speedWaiver;
	}
	
	public int getRevBang()
	{
		return revBang;
	}
	
	public void ResetCar()
	{
		speed = 0;
		gear = 1;
		health = 300;
		totalHealth = health;
		pause = 0;
		countdown = 1000;
		speedWaiver = (int)(Math.random() * 10 - 5);
		coastCount = 50;
		grassCount = 1;
		grassHealthCount = 30;
		revBang = 0;
		bangCount = 20;
		boomCount = 0;
		shiftLight = false;
		exploded = false;
	}
	
	public void OnGrass()
	{
		if(grassCount == 0)
		{
			if(speed > 5 + 5 * gear)
			{
				speed -= 2;
				grassCount = 1;
			}
		}
		else
		{
			grassCount--;
		}
		if(grassHealthCount == 0)
		{
			health--;
			grassHealthCount = 30;
		}
		else
		{
			grassHealthCount--;
		}
	}
	
	public void Collide(int otherCarSpeed, double otherCarX, double otherCarY)
	{
		if(amPlayer)
		{
			crash.play();
			health -= Math.abs(speed - otherCarSpeed);
			// Check if collided from the side
			if(y < otherCarY + h || y - h > otherCarY)
			{
				if(x < otherCarX)
				{
					x -= 5;
				}
				if(x > otherCarX)
				{
					x += 5;
				}
			}
		}
		speed = otherCarSpeed;
	}
	
	public void Accelerate()
	{
		// Accelerates at different rates to different top speeds in different gears
		if(pause == 0)
		{
			if(speed < 0)
			{
				speed = 0;
			}
			switch(gear)
			{
				case 1:
					if(speed < 5)
					{
						speed += 1;
						break;
					}
					else if(speed < 10)
					{
						speed += 2;
						break;
					}
					else if(speed < 15)
					{
						if(!shiftLight)
							shiftLight = true;
						speed += 3;
						break;
					}
					else if(speed < 18)
					{
						if(!shiftLight)
							shiftLight = true;
						speed -= 1;
						if(bangCount <= 0)
						{
							revBang++;
							bang.play();
							bangCount = 20;
						}
						else
						{
							bangCount--;
						}
						break;
					}
					else
					{
						speed -= 5;
						bangCount -= 3;
					}
					break;
				case 2:
					if(speed < 20)
					{
						speed += 1;
						break;
					}
					else if(speed < 30)
					{
						if(!shiftLight)
							shiftLight = true;
						speed += 2;
						break;
					}
					else if(speed < 60)
					{
						if(!shiftLight)
							shiftLight = true;
						speed += 3;
						break;
					}
					else if(speed < 65)
					{
						if(!shiftLight)
							shiftLight = true;
						speed -= 2;
						if(bangCount <= 0)
						{
							revBang++;
							bang.play();
							bangCount = 20;
						}
						else
						{
							bangCount--;
						}
						break;
					}
					else
					{
						speed -= 5;
						bangCount -= 3;
					}
					break;
				case 3:
					if(speed < 25 && speed > 15)
					{
						speed += 1;
						break;
					}
					else if(speed < 45 && speed > 15)
					{
						if(!shiftLight)
							shiftLight = true;
						speed += 2;
						break;
					}
					else if(speed < 75 && speed > 15)
					{
						if(!shiftLight)
							shiftLight = true;
						speed += 3;
						break;
					}
					else if(speed < 77 && speed > 15)
					{
						if(!shiftLight)
							shiftLight = true;
						speed -= 2;
						if(bangCount <= 0)
						{
							revBang++;
							bang.play();
							bangCount = 20;
						}
						else
						{
							bangCount--;
						}
						break;
					}
					else if(speed > 0)
					{
						speed -= 3;
						bangCount -= 3;
						if(!amPlayer)
							ShiftDown();
					}
					break;
				case 4:
					if(speed < 40 && speed > 20)
					{
						speed += 1;
						break;
					}
					else if(speed < 50 && speed > 20)
					{
						if(!shiftLight)
							shiftLight = true;
						speed += 2;
						break;
					}
					else if(speed < 90 && speed > 20)
					{
						if(!shiftLight)
							shiftLight = true;
						speed += 3;
						break;
					}
					else if(speed < 92 && speed > 15)
					{
						if(!shiftLight)
							shiftLight = true;
						speed -= 2;
						if(bangCount <= 0)
						{
							revBang++;
							bang.play();
							bangCount = 20;
						}
						else
						{
							bangCount--;
						}
						break;
					}
					else if(speed > 0)
					{
						speed -= 3;
						bangCount -= 3;
						if(!amPlayer)
							ShiftDown();
					}
					break;
				case 5:
					if(speed < 55 && speed > 35)
					{
						speed += 1;
						break;
					}
					else if(speed < 85 && speed > 35)
					{
						if(!shiftLight)
							shiftLight = true;
						speed += 2;
						break;
					}
					else if(speed < 120 && speed > 35)
					{
						if(!shiftLight)
							shiftLight = true;
						speed += 3;
						break;
					}
					else if(speed < 121 && speed > 15)
					{
						if(!shiftLight)
							shiftLight = true;
						speed -= 2;
						if(bangCount <= 0)
						{
							revBang++;
							bang.play();
							bangCount = 20;
						}
						else
						{
							bangCount--;
						}
						break;
					}
					else if(speed > 0)
					{
						speed -= 3;
						bangCount--;
						if(!amPlayer)
							ShiftDown();
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
			if(speed < 0)
			{
				speed = 0;
			}
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
						if(!amPlayer)
							ShiftDown();
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
						if(!amPlayer)
							ShiftDown();
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
						if(!amPlayer)
							ShiftDown();
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
						if(!amPlayer)
							ShiftDown();
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
		if(speed < 0)
		{
			speed = 0;
		}
		if(speed > 0 && coastCount == 0)
		{
			speed--;
			if(revBang > 0)
			{
				revBang--;
				bangCount = 20;
			}
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
		{
			if(speed < 20)
				x -= 3;
			else if(speed < 65)
				x -= 2;
			else
				x--;
		}
	}
	
	public void TurnRight()
	{
		if(x < Driver.SCREEN_WIDTH - w & speed > 0)
		{
			if(speed < 20)
				x += 3;
			else if(speed < 65)
				x += 2;
			else
				x++;
		}
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
	
	public void draw(Graphics g)
	{
		if(getHealth() > 0)
			super.draw(g);
		else
		{
			if(boomCount < 23)
			{
				g.drawImage(boom.nextImage(), (int)x, (int)y, null);
				boomCount++;
				if(!exploded)
				{
					explode.play();
					exploded = true;
				}
			}
		}
	}
}
