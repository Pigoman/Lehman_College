import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import javax.swing.JPanel;

import java.util.Date;
import java.text.SimpleDateFormat;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

/* Where the drawing happens */

public class BTPCenter extends JPanel implements MouseListener, MouseMotionListener, KeyListener
{
	protected static int 
	lastX, 
	lastY, 
	red = 0, 
	grn = 0, 
	blu = 0,
	thick = 15,
	fontStyle = Font.PLAIN;
	
	protected static String 
	toDrawShape = "No Shape",
	whichFont = Font.SERIF;
	
	protected static Font font = new Font(whichFont, fontStyle, thick);
	protected static FontMetrics fm;
	
	protected static boolean toClear = false;
	
	public BTPCenter()
	{
		setBackground(Color.white);
		addMouseListener(this);
		addMouseMotionListener(this);
		addKeyListener(this);
		fm = getFontMetrics(font);
	}
	
	/*private static void save()
	{
		BufferedImage image = new BufferedImage(this.getWidth(), this.getHeight(), BufferedImage.TYPE_INT_RGB);
		Graphics2D g = image.createGraphics();
		this.printAll(g);
		g.dispose();
		String timeStamp = new SimpleDateFormat("yyyy.MM.dd.HH.mm.ss").format(new Date());
		try
		{
			ImageIO.write(image, "jpg", new File(timeStamp + ".jpg"));
			System.out.println("Saved!");
		}
		catch (IOException exp) 
		{
			System.out.println("Not Saved!");
			exp.printStackTrace();
		}
	}*/
	
	// Record the mouse position
	protected void record(int x, int y){
		lastX = x;
		lastY = y;
	}
	
	/* KeyListener */
	@Override
	public void keyTyped(KeyEvent e) 
	{
		// Type text
		String c = String.valueOf(e.getKeyChar());
		Graphics g = getGraphics();
		Graphics g2d = (Graphics2D)g;
		g2d.setColor(new Color(red, grn, blu));
		g2d.setFont(new Font(whichFont, fontStyle, thick));
		fm = getFontMetrics(new Font(whichFont, fontStyle, thick));
		g2d.drawString(c, lastX, lastY);
		record(lastX+fm.stringWidth(c) + 8, lastY);
	}
	
	@Override
	public void keyPressed(KeyEvent e) 
	{
	}
	
	@Override
	public void keyReleased(KeyEvent e) 
	{
	}
	
	/* MouseMotionListener */
	@Override
	public void mouseDragged(MouseEvent e) 
	{
		// Draw line
		int x = e.getX();
		int y = e.getY();
		Graphics g = getGraphics();
		Graphics g2d = (Graphics2D)g;
		((Graphics2D) g2d).setStroke(new BasicStroke(thick));
		g2d.setColor(new Color(red, grn, blu));
		g2d.drawLine(lastX, lastY, x, y);
		record(x,y);
	}
	
	@Override
	public void mouseMoved(MouseEvent e) 
	{
		// Keep track of mouse position to avoid connecting lines unintentionally
		record(e.getX(), e.getY());
	}
	
	/* MouseListener */
	@Override
	public void mousePressed(MouseEvent e) 
	{
		// Draw shape
		Graphics g = getGraphics();
		Graphics2D g2d = (Graphics2D)g;
		g2d.setColor(new Color(red, grn, blu));
		
		if(toDrawShape.equals("Circle"))
		{
			g2d.fillOval(lastX-(thick/2), lastY-(thick/2), thick, thick);
		}
		if(toDrawShape.equals("Square"))
		{
			g2d.fillRect(lastX-(thick/2), lastY-(thick/2), thick, thick);
		}
	}
	
	@Override
	public void mouseClicked(MouseEvent e) 
	{
	}
	
	@Override
	public void mouseReleased(MouseEvent e) 
	{
	}

	@Override
	public void mouseEntered(MouseEvent e) 
	{
		requestFocusInWindow();
		if(toClear)
		{
			repaint();
			toClear = false;
		}
	}

	@Override
	public void mouseExited(MouseEvent e) 
	{
	}
}
