#
#  This is a simple piece of code designed to generate wavetables.
#
#  The intended application is for a small PIC micocontroller project, in which
# integer wavetables are referenced to produce synthesized tones using an R2R ladder.
#
#  Of course you're free to disect and use this code for whatever you like.
#

import math

#
#  All of the following waveforms are designed to be in-phase with eachother.
#
#  The wave function inputs should be within 0 <= X < 1; At 1 they wrap back around to 0.
# Their outputs will always be be -1 <= Y <= 1
#

def Waveform_Sine( theta ):
    """ Sine wave """
    return math.sin( theta * math.pi * 2 )

def Waveform_Triangle( theta ):
    """ Triangle wave """
    return abs( ( ( ( theta + 0.75 ) * 4 ) % 4 ) - 2 ) - 1

def Waveform_Sawtooth( theta ):
    """ Forward facing sawtooth wave """
    return ( ( theta + 0.5 ) % 1 ) * 2 - 1

def Waveform_Wastooth( theta ):
    """ Backwards facing sawtooth wave """
    return ( 1 - ( theta % 1 ) ) * 2 - 1

def Waveform_Square( theta ):
    """ Square wave """
    return ( theta % 1 < 0.5 ) and 1 or -1


def Wavetable_Generate_Bipolar( waveform, length, depth, phase = 0 ):
    
    """
    Generate a unipolar ( between -1 and 1 ) table of
    floating-point values representing a desired waveform.

    Args:
        waveform: The Function used to generate a waveform.
        length: The number of samples to render.
        depth: The maximum scale of a sample, from +depth to -depth inclusive.
        phase: ( Optional ) The offset of a sample in degrees, 0 - 360.

    Returns:
        array: List of floating-point numbers approximating a waveform.
    """
        
    generatedWavetable = []
    
    for I in range( length ):
        generatedWavetable.append( waveform( I / length + phase / 360 ) * depth )
        
    return generatedWavetable


def Wavetable_Generate_Unipolar( waveform, length, depth, phase = 0 ):
    
    """
    Generate a unipolar ( between 0 and 1 ) table of
    floating-point values representing a desired waveform.

    Args:
        waveform: The Function used to generate a waveform.
        length: The number of samples to render.
        depth: The maximum scale of a sample, from +depth to -depth inclusive.
        phase: ( Optional ) The offset of a sample in degrees, 0 - 360.

    Returns:
        array: List of floating-point numbers approximating a waveform.
    """
        
    generatedWavetable = []
    
    for I in range( length ):
        generatedWavetable.append( ( waveform( I / length + phase / 360 ) + 1 ) / 2 * depth )
        
    return generatedWavetable


def Wavetable_Print_Floating( generatedWavetable ):
    """ Print the unmodified wavetable """
    output = ""
    for sample in generatedWavetable:
        output += str( sample ) + ", ";
    
    print( output )


def Wavetable_Print_Truncated( generatedWavetable ):
    """ Print a rounded integer version of the wavetable """
    output = ""
    for sample in generatedWavetable:
        output += str( round( sample ) ) + ", ";
        
    print( output )


def Wavetable_Print_Hexadecimal( generatedWavetable ):
    """ Print a rounded hexadecimal version of the wavetable """
    output = ""
    for sample in generatedWavetable:
        output += str( hex( round( sample ) ) ) + ", ";

    print( output )

#
# Some usage examples...
#

# Generate a 16-number long triangle wavetable between -15 and 15.
myWavetable = Wavetable_Generate_Bipolar( Waveform_Triangle, 16, 15 )

# Print myWavetable as a list of integers.
Wavetable_Print_Truncated( myWavetable )

# Generate a 32-number long inverted sawtooth wavetable between 0 and 64.
myBiggerWavetable = Wavetable_Generate_Unipolar( Waveform_Wastooth, 32, 64 )

# Print myBiggerWavetable as a list of hexadecimal numbers.
Wavetable_Print_Hexadecimal( myBiggerWavetable )

#
#  If you're interested in learning more about oscillators and wavetables,
# 'https://en.wikibooks.org/wiki/Sound_Synthesis_Theory/Oscillators_and_Wavetables'
# has a lot of valuable information regarding both; including implementations and the math behind each waveform.
#
