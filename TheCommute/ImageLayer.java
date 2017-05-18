import java.awt.*;

public class ImageLayer
{
	Image image;
	
	double x;
	double y;
	double z;
	
	int w;
	
	public ImageLayer(String fileName, double x, double y, double z, int w)
	{
		image = Toolkit.getDefaultToolkit().getImage(fileName + ".png");
		
		this.x = x;
		this.y = y;
		this.z = z;
		
		this.w = w;
	}
	
	public void setX(int newX)
	{
		x = newX;
	}
	
	public void setY(int newY)
	{
		y = newY;
	}
	
	public void draw(Graphics g)
	{
		//for(int i = 0; i < 50; i++)
		g.drawImage(image, (int)(x - Camera2D.x), (int)(y - Camera2D.y), null);
		//g.drawString("x:"+x+" y:"+y, (int)(x - Camera2D.x), (int)(y - Camera2D.y));
	}
}
