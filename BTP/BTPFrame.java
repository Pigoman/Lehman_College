import java.awt.BorderLayout;
import javax.swing.JFrame;
import javax.swing.JPanel;

import java.util.Date;
import java.text.SimpleDateFormat;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class BTPFrame extends JFrame
{
	public BTPFrame()
	{
		setTitle("Better Than Paint!   By Sean Curran");
		// Create JPanel to stick things to
		JPanel mainContent = new JPanel();
		mainContent.setLayout(new BorderLayout());
		
		// Create panels for program
		BTPNorth  NP = new BTPNorth();
		BTPSouth  SP = new BTPSouth();
		BTPEast   EP = new BTPEast();
		BTPWest   WP = new BTPWest();
		BTPCenter CP = new BTPCenter();
		
		// Add the panels to the main panel
		mainContent.add(BorderLayout.NORTH, NP);
		mainContent.add(BorderLayout.SOUTH, SP);
		mainContent.add(BorderLayout.EAST, EP);
		mainContent.add(BorderLayout.WEST, WP);
		mainContent.add(BorderLayout.CENTER, CP);
		
		// Add JPanel to JFrame, set size and display
		add(mainContent);
		setSize(500,500);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
	}
	
	/*
	protected static void save()
	{
		BufferedImage image = new BufferedImage(CP.getWidth(), CP.getHeight(), BufferedImage.TYPE_INT_RGB);
		Graphics2D g = image.createGraphics();
		CP.printAll(g);
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
	}
	*/
}
