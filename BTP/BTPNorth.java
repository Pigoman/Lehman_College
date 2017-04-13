import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class BTPNorth extends JPanel implements ActionListener
{
	public BTPNorth()
	{
		setBackground(Color.gray);
		JLabel title = new JLabel("Options: ");
		add(title);
		
		JButton SaveImage = new JButton("Save");
		SaveImage.addActionListener(this);
		//add(SaveImage);
		
		JButton ClearImage = new JButton("Clear");
		ClearImage.addActionListener(this);
		add(ClearImage);
	}
	
	public void actionPerformed(ActionEvent e)
	{
		//System.out.println("Button Pressed");
		if(e.getActionCommand().equals("Save"))
		{
			//System.out.println("Save Pressed");
		}
		if(e.getActionCommand().equals("Clear"))
		{
			//System.out.println("Clear Pressed");
			BTPCenter.toClear = true;
		}
		//BTPCenter.save();
	}
}
