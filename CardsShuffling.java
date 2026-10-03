//not sure I put the "Classic" files in the same place
package com.example.cards;

import java.awt.*;
import java.util.ArrayList;
import javax.swing.*;
import java.util.Collections;
import java.awt.BorderLayout;

public class Cards {

    private class Card {
        String value;
        String type;


        Card(String value, String type) {
            this.value = value;
            this.type = type;
        }

    }

    int cardWidth = 70;
    int cardHeight = 110;

    ArrayList<Card> deck;

    JFrame frame = new JFrame("Card Shuffler");

    JPanel gamePanel = new JPanel()
    {
        @Override
        public void paintComponent(Graphics g)
        {
            super.paintComponent(g);

            for (int i = 0; i < deck.size(); i++)
            {

                Card current = deck.get(i);

                String folder = "/Classic/" + current.type + current.value + ".png";
                System.out.println(getClass().getResource("/Classic/c01.png"));

                Image image = new ImageIcon(getClass().getResource(folder)).getImage();

                int drawX = 30 + (i % 13) * 80;
                int drawY = 30 + (i / 13) * 150;

                g.drawImage(image, drawX,drawY, cardWidth, cardHeight, null);
            }
        }

    };

    Cards() {
        buildDeck();
        //color for table
        Color tableGreen = new Color(0,100,0);
        gamePanel.setBackground(tableGreen);

        frame.add(gamePanel);

        //creates shuffle button
        JButton shuffleButton = new JButton("Shuffle Cards");
        shuffleButton.addActionListener(e -> {
            Collections.shuffle(deck);
            gamePanel.repaint();
        });

        JPanel bottomPanel = new JPanel();
        bottomPanel.setBackground(tableGreen);

        bottomPanel.setBorder(BorderFactory.createEmptyBorder(10,10,25,10));
        bottomPanel.add(shuffleButton);
        frame.setLayout(new BorderLayout());
        frame.add(gamePanel, BorderLayout.CENTER);
        frame.add(bottomPanel, BorderLayout.SOUTH);

        frame.setSize(1100, 750);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }


    public void buildDeck() {
        deck = new ArrayList<Card>();

        String[] values = {
                "01", "02", "03", "04", "05", "06", "07",
                "08", "09", "10", "11", "12", "13"
        };

        String[] types = {
                "c", "d", "s", "h"
        };

        for (int i = 0; i < types.length; i++) {
            for (int j = 0; j < values.length; j++) {
                Card card = new Card(values[j], types[i]);
                deck.add(card);
            }
        }

    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new Cards();
        });
    }
}
