/*
Build on the previous homework so that the center panel, draws lines, shapes, 
   character in response to mouseDragged, mousePressed, keyTyped.
The user should be able to control the size, and color of all the shapes, lines, 
   and letters through the use of various JComponents.
Presenting on Monday February 27th will earn you 5 extra points.
Late projects will not be accepted. 
Not presenting your work will cause a deduction of 10 points.
*/

/*
Got drawings
Got shapes
Got writing, but font is buggy. Think it's Java in general, must investigate
Finish South Panel with fonts
Put clear and save buttons in North panel
Save files with timestamp as name?
*/

public class BTPDriver
{
	public static void main(String[] args)
	{
		// Create separate thread to run GUI in
		javax.swing.SwingUtilities.invokeLater(new Runnable() 
		{
			@Override
			public void run() 
			{
				BTPFrame myGUI = new BTPFrame();
			}
		});
	}
}
