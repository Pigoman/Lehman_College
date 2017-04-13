import java.awt.Color;
import java.awt.Font;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

/* Typing and font */

public class BTPSouth extends JPanel implements ItemListener, ActionListener
{
	JCheckBox bold, italic;
	JTextField fontName;
	JButton setFont;
	
	public BTPSouth()
	{
		setBackground(Color.gray);
		setLayout(new FlowLayout(FlowLayout.LEFT));
		//JLabel title = new JLabel("South Panel!");
		JLabel title = new JLabel("Select a Font: ");
		add(title);
		
		fontName = new JTextField(20);
		add(fontName);
		
		setFont = new JButton("Set Font!");
		setFont.addActionListener(this);
		add(setFont);
		
		bold = new JCheckBox("Bold");
		bold.addItemListener(this);
		add(bold);
		
		italic = new JCheckBox("Italic");
		italic.addItemListener(this);
		add(italic);
	}
	
	public void actionPerformed(ActionEvent e)
	{
		BTPCenter.whichFont = fontName.getText();
	}

	public void itemStateChanged(ItemEvent e)
	{
		Object source = e.getItemSelectable();
		if(source == bold && e.getStateChange() == ItemEvent.SELECTED)
		{
			BTPCenter.fontStyle += Font.BOLD;
		}
		if(source == bold && e.getStateChange() == ItemEvent.DESELECTED)
		{
			BTPCenter.fontStyle -= Font.BOLD;
		}
		if(source == italic && e.getStateChange() == ItemEvent.SELECTED)
		{
			BTPCenter.fontStyle += Font.ITALIC;
		}
		if(source == italic && e.getStateChange() == ItemEvent.DESELECTED)
		{
			BTPCenter.fontStyle -= Font.ITALIC;
		}
	}
}
