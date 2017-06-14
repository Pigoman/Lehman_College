import java.io.*;
import java.net.URL;
import javax.sound.sampled.*;

public class Audio
{
	private Clip audio;

	// Audio
	public Audio(String file)
	{
		AudioInputStream audioIn;
		
		// URL location for the audio files.
		URL fileUrl = this.getClass().getClassLoader().getResource(file);
		//System.out.println(fileUrl);

		// Open audio input streams.
		try
		{
			// Load the audio files
			audioIn = AudioSystem.getAudioInputStream(fileUrl);
			DataLine.Info info = new DataLine.Info(Clip.class, audioIn.getFormat());
			this.audio = (Clip)AudioSystem.getLine(info);
			this.audio.open(audioIn);
			
			// Get a sound clip resource.
			//this.audio = AudioSystem.getClip();

			// Open audio clip and load samples from the audio input stream.
			//this.audio.open(audioIn);

		} 
		catch (UnsupportedAudioFileException e) 
		{
			System.out.println("Unsupported file: " + file);
			e.printStackTrace();
		} 
		catch (IOException e) 
		{
			System.out.println("IO Exception: " + file);
			e.printStackTrace();
		} 
		catch (LineUnavailableException e) 
		{
			System.out.println("Line Unavailable: " + file);
			e.printStackTrace();
		}
	}

	// Play One Time
	public void play() 
	{
		audio.loop(0);
		reset();
		/*
		if(audio.isRunning()) 
		{
			// Stop the player if it is still running
			stop();

			// Rewind to the beginning
			reset();
			//audio.start();
			audio.loop(1);
		}
		else 
		{
			// rewind to the beginning
			//audio.setMicrosecondPosition(0);
			//reset();
			//audio.start();
			audio.loop(1);
		}
		*/
	}

	// Play As Loop
	public void playLoop() 
	{
		// Rewind the audio track to the beginning
		//reset();
		audio.loop(Clip.LOOP_CONTINUOUSLY);
	}
	
	// Control
	public void stop()   
	{ 
		audio.stop();
	}
	public void pause()  
	{ 
		stop();
	}
	public void unPause()
	{ 
		//audio.start();
		audio.loop(1);
	}
	public void reset()
	{ 
		audio.setMicrosecondPosition(0);
	}

}
