import math

def enum(*sequential, **named):
  enums = dict(zip(sequential, range(len(sequential))), **named)
  return type('Enum', (), enums)

Operations = enum('ADDITION', 'SUBTRACTION', 'DIVISION', 'MULTIPLICATION', 'LOG', 'EQUALS')

class InputError(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

class EvaluationError(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

def sign(number):
  if number >= 0:
    return 1
  else:
    return -1

class Calculator:
  """A calculator class"""

  def __init__(self):
    self.inMemoryNumber = 0.
    self.inputNumber = 0.
    self.inputPosition = 0
    self.operation =  Operations.EQUALS

  def inputDigit(self, digit):
    if isinstance(digit, (int,long)) and digit >= 0 and digit <= 9:
      if self.inputPosition == 0:
        self.inputNumber *= 10.
        self.inputNumber += float(digit) * sign(self.inputNumber)
      else:
        self.inputNumber += float(digit) * sign(self.inputNumber) / (10 ** self.inputPosition)
        self.inputPosition += 1
    else:
      raise InputError('Digits can only be integers in diapasone 0..9')

  def _add(self):
    self.inMemoryNumber += self.inputNumber

  def _subtract(self):
    self.inMemoryNumber -= self.inputNumber

  def _divide(self):
    if self.inputNumber != 0:
      self.inMemoryNumber /= self.inputNumber
    else:
      raise EvaluationError('Division by zero')

  def _multiply(self):
    self.inMemoryNumber *= self.inputNumber

  def _log(self):
    if self.inMemoryNumber > 0 and self.inputNumber > 0:
      self.inMemoryNumber = math.log(self.inputNumber, self.inMemoryNumber)
    else:
      raise EvaluationError('Log of invalid values')

  def _equals(self):
    self.inMemoryNumber = self.inputNumber

  def click_dot(self):
    if self.inputPosition == 0:
      self.inputPosition = 1

  def execute_operation(self, operation):
    {
      Operations.ADDITION: self._add,
      Operations.SUBTRACTION: self._subtract,
      Operations.MULTIPLICATION: self._multiply,
      Operations.DIVISION: self._divide,
      Operations.LOG: self._log,
      Operations.EQUALS: self._equals
    }[self.operation]()
    self.inputNumber = 0.
    self.inputPosition  = 0
    self.operation = operation
