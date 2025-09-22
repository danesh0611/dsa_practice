import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class FormDesignApplet extends JFrame {

    public FormDesignApplet() {
       
        setTitle("Form Design");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);  // Center the window
        setLayout(new FlowLayout());

    
        JLabel nameLabel = new JLabel("Name:");
        JTextField nameTextField = new JTextField(15);
        JLabel ageLabel = new JLabel("Age:");
        JTextField ageTextField = new JTextField(5);
        JButton submitButton = new JButton("Submit");

      
        add(nameLabel);
        add(nameTextField);
        add(ageLabel);
        add(ageTextField);
        add(submitButton);

        submitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = nameTextField.getText();
                String age = ageTextField.getText();
                JOptionPane.showMessageDialog(null, "Name: " + name + "\nAge: " + age);
            }
        });
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                
          new FormDesignApplet().setVisible(true);
            }
        });
    }
}
