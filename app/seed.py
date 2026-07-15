import json
from app import db
from app.models import MindfulnessExercise


def seed_mindfulness_exercises():
    """Seed database with mindfulness exercises if empty."""
    if MindfulnessExercise.query.first():
        return

    exercises = [
        # Breathing - Beginner
        {
            'title': '4-7-8 Breathing',
            'category': 'breathing',
            'difficulty': 'beginner',
            'duration_minutes': 5,
            'description': 'A calming breathing pattern that helps reduce anxiety and promote relaxation.',
            'steps': json.dumps([
                'Find a comfortable seated position and close your eyes.',
                'Exhale completely through your mouth, making a whoosh sound.',
                'Close your mouth and inhale quietly through your nose for 4 seconds.',
                'Hold your breath for 7 seconds.',
                'Exhale completely through your mouth for 8 seconds.',
                'This is one breath cycle. Repeat 3 more times for a total of 4 cycles.'
            ])
        },
        # Breathing - Intermediate
        {
            'title': 'Box Breathing',
            'category': 'breathing',
            'difficulty': 'intermediate',
            'duration_minutes': 8,
            'description': 'Used by Navy SEALs for stress management. Equal-length inhale, hold, exhale, hold pattern.',
            'steps': json.dumps([
                'Sit upright in a comfortable chair with feet flat on the floor.',
                'Slowly exhale all the air from your lungs.',
                'Inhale slowly through your nose for 4 seconds, filling your lungs completely.',
                'Hold your breath for 4 seconds. Stay calm and relaxed.',
                'Exhale slowly through your mouth for 4 seconds.',
                'Hold your breath (lungs empty) for 4 seconds.',
                'Repeat this cycle for 5-8 minutes.',
                'Gradually increase hold times to 5 or 6 seconds as you improve.'
            ])
        },
        # Breathing - Advanced
        {
            'title': 'Alternate Nostril Breathing',
            'category': 'breathing',
            'difficulty': 'advanced',
            'duration_minutes': 10,
            'description': 'A yogic breathing technique (Nadi Shodhana) that balances the nervous system.',
            'steps': json.dumps([
                'Sit comfortably with your spine straight.',
                'Place your left hand on your left knee, palm open.',
                'Bring your right hand to your nose — use thumb for right nostril, ring finger for left.',
                'Close your right nostril with your thumb. Inhale through the left nostril for 4 seconds.',
                'Close both nostrils and hold for 4 seconds.',
                'Release right nostril, keep left closed. Exhale through right for 4 seconds.',
                'Inhale through the right nostril for 4 seconds.',
                'Close both nostrils and hold for 4 seconds.',
                'Release left nostril, keep right closed. Exhale through left for 4 seconds.',
                'This completes one full cycle. Continue for 5-10 cycles.'
            ])
        },
        # Meditation - Beginner
        {
            'title': 'Mindful Awareness Meditation',
            'category': 'meditation',
            'difficulty': 'beginner',
            'duration_minutes': 5,
            'description': 'A simple meditation to develop present-moment awareness.',
            'steps': json.dumps([
                'Find a quiet, comfortable place to sit.',
                'Set a timer for 5 minutes.',
                'Close your eyes and take 3 deep breaths.',
                'Bring your attention to the sensation of breathing — notice the air entering and leaving.',
                'When your mind wanders (it will!), gently return focus to your breath.',
                'Don\'t judge yourself for wandering thoughts. Simply notice and return.',
                'When the timer sounds, slowly open your eyes and take one more deep breath.'
            ])
        },
        # Meditation - Intermediate
        {
            'title': 'Loving-Kindness Meditation',
            'category': 'meditation',
            'difficulty': 'intermediate',
            'duration_minutes': 10,
            'description': 'Cultivate compassion for yourself and others through directed well-wishes.',
            'steps': json.dumps([
                'Sit comfortably and close your eyes. Take several deep breaths.',
                'Begin by directing kindness toward yourself. Repeat: "May I be happy. May I be healthy. May I be safe."',
                'Now think of someone you love. Direct kindness toward them: "May you be happy. May you be healthy. May you be safe."',
                'Think of a neutral person (a stranger). Send them the same wishes.',
                'Think of someone difficult. Try sending them the same compassion.',
                'Finally, extend these wishes to all beings: "May all beings be happy. May all beings be healthy. May all beings be safe."',
                'Sit with the feeling of universal compassion for 2 minutes.',
                'Slowly open your eyes and carry this feeling with you.'
            ])
        },
        # Meditation - Advanced
        {
            'title': 'Emotion Observation Meditation',
            'category': 'meditation',
            'difficulty': 'advanced',
            'duration_minutes': 15,
            'description': 'Observe and accept emotions without attachment or judgment.',
            'steps': json.dumps([
                'Find a quiet space and sit comfortably. Set a timer for 15 minutes.',
                'Close your eyes and spend 2 minutes following your breath.',
                'Now shift attention to your emotional state. What are you feeling right now?',
                'Name the emotion without judging it: "I notice anxiety" or "There is sadness here."',
                'Notice where in your body you feel this emotion. Observe the physical sensation.',
                'Imagine the emotion as a cloud passing through the sky of your mind.',
                'Don\'t try to push it away or hold onto it. Simply observe.',
                'If a new emotion arises, name it and observe it in the same way.',
                'When thoughts pull you into stories about the emotion, return to observing.',
                'In the last 2 minutes, return attention to your breath.',
                'Open your eyes slowly, carrying this non-judgmental awareness forward.'
            ])
        },
        # Body Scan - Beginner
        {
            'title': 'Quick Body Check-In',
            'category': 'body_scan',
            'difficulty': 'beginner',
            'duration_minutes': 5,
            'description': 'A brief body scan to release tension and connect with your physical state.',
            'steps': json.dumps([
                'Lie down or sit comfortably. Close your eyes.',
                'Take 3 deep breaths to settle in.',
                'Notice your feet — any tension or sensation? Breathe into that area.',
                'Move attention to your legs and hips. Notice and release any tension.',
                'Bring awareness to your stomach and chest. Notice your breathing.',
                'Scan your shoulders, arms, and hands. Let them relax.',
                'Notice your neck, face, and head. Soften your jaw and forehead.',
                'Take one final deep breath, feeling your whole body at once. Open your eyes.'
            ])
        },
        # Body Scan - Intermediate
        {
            'title': 'Progressive Muscle Relaxation',
            'category': 'body_scan',
            'difficulty': 'intermediate',
            'duration_minutes': 12,
            'description': 'Systematically tense and release muscle groups to reduce physical stress.',
            'steps': json.dumps([
                'Lie down comfortably. Take 5 slow, deep breaths.',
                'Curl your toes tightly for 5 seconds. Release and notice the difference. Breathe.',
                'Tense your calf muscles for 5 seconds. Release. Breathe.',
                'Squeeze your thighs for 5 seconds. Release. Breathe.',
                'Tighten your abdomen for 5 seconds. Release. Breathe.',
                'Make fists with both hands for 5 seconds. Release. Breathe.',
                'Tense your biceps (curl arms) for 5 seconds. Release. Breathe.',
                'Shrug your shoulders up to your ears for 5 seconds. Release. Breathe.',
                'Scrunch your face tightly for 5 seconds. Release. Breathe.',
                'Now scan your whole body for any remaining tension. Breathe into those areas.',
                'Rest in this relaxed state for 2 minutes, noticing how your body feels.'
            ])
        },
        # Body Scan - Advanced
        {
            'title': 'Deep Body Scan with Visualization',
            'category': 'body_scan',
            'difficulty': 'advanced',
            'duration_minutes': 20,
            'description': 'A thorough body scan combining physical awareness with healing visualization.',
            'steps': json.dumps([
                'Lie down in a comfortable position. Close your eyes and take 5 deep breaths.',
                'Imagine a warm, golden light hovering above the top of your head.',
                'Let the light flow into your head, relaxing your scalp, forehead, and temples.',
                'The light moves to your eyes, cheeks, jaw — releasing all tension.',
                'It flows down your neck and throat, warming and softening.',
                'The light spreads across your shoulders and down both arms to your fingertips.',
                'Feel it fill your chest, warming your heart center. Breathe deeply.',
                'The light flows into your abdomen, releasing any held emotions.',
                'It moves through your lower back and hips, soothing and releasing.',
                'The warm light flows down your thighs, knees, calves, and into your feet.',
                'Your entire body is now filled with warm, healing light.',
                'Stay here for 5 minutes, breathing slowly, feeling completely at peace.',
                'Slowly begin to wiggle your fingers and toes.',
                'Take a deep breath and gently open your eyes when ready.'
            ])
        }
    ]

    for ex_data in exercises:
        exercise = MindfulnessExercise(**ex_data)
        db.session.add(exercise)

    db.session.commit()