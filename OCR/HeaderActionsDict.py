#符文標頭對應字典
from OCR.TextJudge import Attack, Defense, Health, Speed, CriticalHit, CriticalHitDamage, Effect

blessingsActions = {
    #祝福符文
    "攻擊速度": Speed,
    "體力": Health,
    "效果命中": Effect,
    "效果抵抗": Effect
}

fierceAttackActions = {
    #猛攻符文
    "攻擊速度": Speed,
    "攻擊力": Attack,
    "暴擊率": CriticalHit,
    "暴擊傷害": CriticalHitDamage,
}

bladeEdgeActions = {
    #刀刃符文
    "攻擊速度": Speed,
    "攻擊力": Attack,
    "暴擊率": CriticalHit,
    "暴擊傷害": CriticalHitDamage,
}

provocationActions = {
    #激怒符文
    "攻擊速度": Speed,
    "攻擊力": Attack,
    "暴擊率": CriticalHit,
    "暴擊傷害": CriticalHitDamage,
}

repaidActions = {
    #迅速符文
    "攻擊速度": Speed,
    "體力": Health,
    "防禦力": Defense,
    "效果命中": Effect,
}

concentrateActions = {
    #集中符文
    "攻擊速度": Speed,
    "體力": Health,
    "效果命中": Effect,
    "效果抵抗": Effect
}

guardActions = {
    #守護符文
    "攻擊速度": Speed,
    "攻擊力": Attack,
    "防禦力": Defense,
    "效果命中": Effect,
}

patienceActions = {
    #忍耐符文
    "攻擊速度": Speed,
    "體力": Health,
    "效果命中": Effect,
    "效果抵抗": Effect
}

rampageActions = {
    #暴走符文
    "攻擊速度": Speed,
    "體力": Health,
    "攻擊力": Attack,
    "暴擊率": CriticalHit,
    "暴擊傷害": CriticalHitDamage,
    "效果命中": Effect,
}

despairActions = {
    #絕望符文
    "攻擊速度": Speed,
    "體力": Health,
    "效果命中": Effect,
    "效果抵抗": Effect
}

bloodsuckActions = {
    #吸血符文
    "攻擊速度": Speed,
    "體力": Health,
    "攻擊力": Attack,
    "暴擊率": CriticalHit,
    "暴擊傷害": CriticalHitDamage,
}

willpowerActions = {
    #意志符文
    "攻擊速度": Speed,
    "體力": Health,
    "攻擊力": Attack,
    "暴擊率": CriticalHit,
    "暴擊傷害": CriticalHitDamage,
}

retributionActions = {
    #應報符文
    "攻擊速度": Speed,
    "體力": Health,
    "攻擊力": Attack,
    "效果命中": Effect,
    "效果抵抗": Effect
}

protectionActions = {
    #保護符文
    "攻擊速度": Speed,
    "體力": Health,
    "防禦力": Defense,
    "效果抵抗": Effect
}

counterattackActions = {
    #反擊符文
    "攻擊速度": Speed,
    "體力": Health,
    "攻擊力": Attack,
    "防禦力": Defense,
    "效果抵抗": Effect
}

destructionActions = {
    #破壞符文
    "攻擊速度": Speed,
    "攻擊力": Attack,
    "暴擊率": CriticalHit,
    "暴擊傷害": CriticalHitDamage,
}

actions = {
    "攻擊速度": Speed,
    "體力": Health,
    "攻擊力": Attack,
    "防禦力": Defense,
    "暴擊率": CriticalHit,
    "暴擊傷害": CriticalHitDamage,
    "效果命中": Effect,
    "效果抵抗": Effect
}
