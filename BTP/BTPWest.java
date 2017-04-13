import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.BoxLayout;
import javax.swing.ButtonGroup;
import javax.swing.JRadioButton;
import javax.swing.JLabel;
import javax.swing.JPanel;

/* Allow the user to click and place shapes */

public class BTPWest extends JPanel implements ActionListener
{

	JRadioButton NoShape, Circle, Square;

	public BTPWest()
	{
		setBackground(Color.lightGray);
		setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
		
		JLabel title = new JLabel("Place A Shape");
		add(title);
		
		NoShape  = new JRadioButton("No Shape", true);
		Circle   = new JRadioButton("Circle");
		Square   = new JRadioButton("Square");
		
		NoShape.addActionListener(this);
		Circle.addActionListener(this);
		Square.addActionListener(this);
		
		ButtonGroup group = new ButtonGroup();
		group.add(NoShape);
		group.add(Circle);
		group.add(Square);
		
		add(NoShape);
		add(Circle);
		add(Square);
	}
	
	public void actionPerformed(ActionEvent e)
	{
		BTPCenter.toDrawShape = e.getActionCommand();
	}
}
