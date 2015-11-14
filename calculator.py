import math
from decimal import *

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

class Calculator:
  """A calculator class"""

  def __init__(self):
    getcontext().prec = 6
    getcontext().traps[DivisionByZero] = 1
    self.inMemoryNumber = Decimal(0)
    self.inputNumber = Decimal(0)
    self.dot = False
    self.operation =  Operations.EQUALS

  def getMemory(self):
    return float(self.inMemoryNumber)

  def getInput(self):
    return float(self.inputNumber)

  def inputDigit(self, digit):
    if isinstance(digit, (int, long)) and digit >= 0 and digit <= 9:
      exponent = self.inputNumber.as_tuple().exponent
      sign = 1 if self.inputNumber.as_tuple().sign == 0 else -1
      if exponent == 0 and not self.dot:
        self.inputNumber = self.inputNumber * Decimal(10)
      if self.dot or exponent < 0:
        exponent -= 1
        self.dot = False
      self.inputNumber = self.inputNumber + Decimal(digit) * Decimal(sign) * (Decimal(10) ** Decimal(exponent))
    else:
      raise InputError('Digits can only be integers in diapasone 0..9')

  def _add(self):
    self.inMemoryNumber += self.inputNumber

  def _subtract(self):
    self.inMemoryNumber -= self.inputNumber

  def _divide(self):
    try:
      self.inMemoryNumber /= self.inputNumber
    except DivisionByZero:
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
    if self.inputNumber.as_tuple().exponent == 0:
      self.dot = True

  def execute_operation(self, operation):
    {
      Operations.ADDITION: self._add,
      Operations.SUBTRACTION: self._subtract,
      Operations.MULTIPLICATION: self._multiply,
      Operations.DIVISION: self._divide,
      Operations.LOG: self._log,
      Operations.EQUALS: self._equals
    }[self.operation]()
    self.inputNumber = Decimal(0)
    self.inputPosition  = Decimal(0)
    self.dot = False
    self.operation = operation
