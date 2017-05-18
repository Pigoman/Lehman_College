import java.awt.*;

public class Sprite extends Rect
{
   Animation[] animation;

   public static final int UP = 0;
   public static final int DN = 1;
   public static final int LT = 2;
   public static final int RT = 3;

   int action = UP;

   boolean moving = false;

   public Sprite
   (
      double      x,
      double      y,
      int      w,
      int      h,
      String   filename,
      int      count,
      int      duration,
      String[] action
   )
   {
      super(x, y, w, h);

      animation = new Animation[action.length];

      for(int i = 0; i < animation.length; i++)
         animation[i] = new Animation(filename + "_" + action[i] + "_" , count, duration);
    }

   public void moveBy(double dx, double dy)
   {
      x += dx;
      y += dy;

      moving = true;
   }

   public void moveLeftBy(double dx)
   {
      x -= dx;

      action = LT;

      //moving = true;
   }

   public void moveRightBy(double dx)
   {
      x += dx;

      action = RT;

      //moving = true;
   }

   public void moveUpBy(double dy)
   {
      y -= dy;

      action = UP;

      //moving = true;
   }

   public void moveDownBy(double dy)
   {
      y+= dy;

      action = DN;

      //moving = true;
   }

   public void draw(Graphics g)
   {
      if(moving)    g.drawImage(animation[action].nextImage(), (int)x, (int)y, null);

      else          g.drawImage(animation[action].staticImage(), (int)x, (int)y, null);

      moving = false;

      //g.drawRect(x, y, w, h);
   }

}
