#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Assignment Week 5 - Object Oriented Programming
======================================================

"""

def main():
    """Main function that executes both activities"""
    print("PYTHON ASSIGNMENT WEEK 5 - OOP")
    print("=" * 50)
    print()
    
    # Importing and executing activities
    try:
        print("Executing Activity 1...")
        print()
        from smartphone import demonstrate_smartphone
        demonstrate_smartphone()
        
        print("\n" + "=" * 80 + "\n")
        
        print("Executing Activity 2...")
        print()
        from polymorphism_challenge import demonstrate_polymorphism
        demonstrate_polymorphism()
        
    except ImportError as e:
        print(f"Error importing modules: {e}")
        print("Make sure all files are in the same directory!")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
