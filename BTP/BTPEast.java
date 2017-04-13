import java.awt.Color;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

/* Set color, size, all that good stuff */

public class BTPEast extends JPanel implements ActionListener
{

	private int
	red = 0,
	grn = 0,
	blu = 0,
	thick = BTPCenter.thick;
	
	JTextField TR, TG, TB, TW;
	JPanel ColorSample;
	
	public BTPEast()
	{
		setBackground(Color.lightGray);
		setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
		
		JLabel L1 = new JLabel("Color Red");
		add(L1);
		
		TR = new JTextField();
		TR.setText(Integer.toString(red));
		TR.setMaximumSize(new Dimension(120, 40));
		add(TR);
		
		JLabel L2 = new JLabel("Color Green");
		add(L2);
		
		TG = new JTextField();
		TG.setText(Integer.toString(grn));
		TG.setMaximumSize(new Dimension(120, 40));
		add(TG);
		
		JLabel L3 = new JLabel("Color Blue");
		add(L3);
		
		TB = new JTextField();
		TB.setText(Integer.toString(blu));
		TB.setMaximumSize(new Dimension(120, 40));
		add(TB);
		
		JButton CB = new JButton("Set it!");
		CB.addActionListener(this);
		add(CB);
		
		JLabel L4 = new JLabel("Color:");
		add(L4);
		
		ColorSample = new JPanel();
		ColorSample.setBackground(new Color(red, grn, blu));
		ColorSample.setMaximumSize(new Dimension(100, 50));
		add(ColorSample);
		
		JLabel L5 = new JLabel("Width");
		add(L5);
		
		TW = new JTextField();
		TW.setText(Integer.toString(thick));
		TW.setMaximumSize(new Dimension(120, 40));
		add(TW);	
	}
	
	public void actionPerformed(ActionEvent e)
	{
		red   = Integer.parseInt(TR.getText());
		grn   = Integer.parseInt(TG.getText());
		blu   = Integer.parseInt(TB.getText());
		thick = Integer.parseInt(TW.getText());
		// Red
		if(red >= 255)
		{
			red = 255;
			BTPCenter.red = 255;
		}
		else if(red < 0)
		{
			red = 0;
			BTPCenter.red = 0;
		}
		else
		{
			BTPCenter.red = red;
		}
		// Green
		if(grn >= 255)
		{
			grn = 255;
			BTPCenter.grn = 255;
		}
		else if(grn < 0)
		{
			grn = 0;
			BTPCenter.grn = 0;
		}
		else
		{
			BTPCenter.grn = grn;
		}
		// Blue
		if(blu >= 255)
		{
			blu = 255;
			BTPCenter.blu = 255;
		}
		else if(blu < 0)
		{
			blu = 0;
			BTPCenter.blu = 0;
		}
		else
		{
			BTPCenter.blu = blu;
		}
		// Set the sample color
		ColorSample.setBackground(new Color(red, grn, blu));
		// Set text boxes if improper numbers
		TR.setText(Integer.toString(red));
		TG.setText(Integer.toString(grn));
		TB.setText(Integer.toString(blu));
		
		// Set new pen thickness
		if (thick < 1)
			thick = 1;
		BTPCenter.thick = thick;
		TW.setText(Integer.toString(thick));
	}
}
