from datetime import date, timedelta, datetime
from Storage import load_json, save_json

class Habit:
    ''' Represent a single habit'''

    def __init__(self, name, description, frequency, created_on=None, last_done=None, is_archived=False):
        self.name = name
        self.description = description
        self.frequency = frequency
        self.created_on = created_on
        self.last_done = last_done
        self.is_archived = is_archived

    def to_dict(self): 
        return{
            "id":self.id,
            "name":self.name,
            "description":self.description,
            "created_on":self.created_on,
            "last_done":self.last_done,
            "is_archived":self.is_archived
        }
    
    def mark_done(self):
        today = date.today().isoformat()
        logs = load_json('Logs.json')

        for log in logs:
            if log["habit_id"]== self.id and log["date"]==today:
                return False, "Already completed today."
            
        new_entry = {
            "habit_id":self.id,
            "date":today
        }
        logs.append(new_entry)
        save_json("Logs.json", logs)
        return True, "Marked as done for today."
    
    def get_logs(self):
        logs = load_json("Logs.json")
        return [log for log in logs if log["habit_id"==self.id]]
    
    def was_done_on(self,date):
        logs = self.get_logs()
        for log in logs:
            if log["date"]==date:
                return True
        return False

    def was_done_today(self):
        today = date.today().isoformat()
        return self.was_done_on(today)

    def last_done_date(self):
        logs = self.get_logs()
        if not logs:
            return None
        
        dates = [datetime.formisoformat(logs["date"]).date() for log in logs]

        streak = 0
        current = date.today()

        while True:
            if current in dates:
                streak +=1
                current -= timedelta(days=1)
            else:
                break
        return streak
    
    def is_due(self):
        if self.frequency =="daily":
            return True
        last = self.last_done_date()
        today = date.today()
        if self.frequency =="weekly":
            if not last :
                return True
            return (today-last).days >=7
        return True

    def is_missing(self):
        return self.is_due() and not self.was_done_today()

    def strike(self):
        logs = self.get_logs()
        if not logs:
            return 0
        
        logs_dates = [datetime.fromisoformat(log["date"]).date() for log in logs]
        streak = 0
        current = date.today()

        while True:
            if current in logs_dates:
                streak += 1
                current -= timedelta(days=1)
            else:
                break
        return streak
         
    def longest_strike(self):
        logs = self.get_logs()
        if not logs:
            return 0
        
        logs_date = sorted([datetime.fromisoformat(log["date"]).date() for log in logs])

        longest = 1
        current_streak = 1

        for i in range(1, len(logs_date)):
            if (logs_date[i] - logs_date(i-1)).days ==1:
                current_streak +=1
            else:
                longest = max(longest,current_streak)
                current_streak = 1
            return max(longest, current_streak)
        
    def success_rate(self):
        logs = self._get_logs()
        if not logs:
            return 0.0

        created = datetime.fromisoformat(self.created_at).date()
        today = date.today()

        total_days = (today - created).days + 1
        completed = len(logs)

        return round((completed / total_days) * 100, 2)
    
class LogEntry:
    ''' Represents a single habit-completionn log. '''
    def __init__(self, habit_id, date_done=None):
        self.habit_id = habit_id
        self.date_done = date_done or str(date.today())

    def to_dict(self):
        return {
            "habit_id": self.habit_id,
            "date_done": self.date_done
            }
        