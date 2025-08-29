//DrawSmiley.java
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JPanel;
import javax.swing.JFrame;

class SmileyPanel extends JPanel {
    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        
        g.setColor(Color.YELLOW);
        g.fillOval(10, 10, 200, 200);

        
        g.setColor(Color.BLACK);
        g.fillOval(55, 65, 30, 30);
        //g.fillOval(135, 65, 30, 30);

       
        g.fillOval(50, 110, 120, 60);

        
        g.setColor(Color.YELLOW);
        g.fillRect(50, 110, 120, 30);
        g.fillOval(50, 120, 120, 40);
    }
}

public class DrawSmiley {  
    public static void main(String[] args) {
        SmileyPanel panel = new SmileyPanel();
        JFrame application = new JFrame("Smiley Face");

        application.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        application.add(panel);
        application.setSize(230, 250);
        application.setVisible(true);
    }
}
