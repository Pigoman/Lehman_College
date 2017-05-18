import java.awt.*;
import java.awt.image.*;

public class BackgroundManager
{
	private static ImageLayer[][] IL;// = new ImageLayer[Driver.SCREEN_WIDTH % 100 + 2][Driver.SCREEN_HEIGHT % 100];
	
	public BackgroundManager(String fileName1, String fileName2, String fileName3)
	{
		IL = new ImageLayer[Driver.SCREEN_WIDTH / 100][Driver.SCREEN_HEIGHT / 100 + 2];
		for(int y = 0; y < IL.length; y++)
		{
			for(int x = 0; x < IL[y].length; x++)
			{
				if(y > 1 && y < 6)
				{
					if(x % 4 == 0)
						IL[y][x] = new ImageLayer(fileName3, y * 100, x * 100, 1, 100); // Concrete white line
					else
						IL[y][x] = new ImageLayer(fileName2, y * 100, x * 100, 1, 100); // Concrete
				}
				else
					IL[y][x] = new ImageLayer(fileName1, y * 100, x * 100, 1, 100); // Grass
			}
		}
	}
	
	public void draw(Graphics g)
	{
		for(int y = 0; y < IL.length; y++)
		{
			for(int x = 0; x < IL[y].length; x++)
			{
				if(IL[y][x].y > Camera2D.y + Driver.SCREEN_HEIGHT)
				{
					IL[y][x].setY((int)(IL[y][x].y - 800));
				}
				IL[y][x].draw(g);
			}
		}
	}
}
