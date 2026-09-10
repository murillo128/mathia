# VIS-139 — disjoint pair-statistic covariance requires four-level information

## Claim

Let `eta` be a simple point process with factorial moment measures `alpha^(r)`, and let

`U_f = sum_(x,y in eta, x!=y) f(x,y)`,

`U_g = sum_(u,v in eta, u!=v) g(u,v)`

be bounded order-two point-process U-statistics. Expanding `E[U_f U_g]` by the number of distinct points shows that their covariance is controlled in general by the second-, third-, and fourth-factorial moment measures.

If `f` is supported on `A x A`, `g` is supported on `B x B`, and `A` and `B` are disjoint, every shared-point contraction vanishes. In that case the exact covariance reduces to

`Cov(U_f,U_g) = integral_(A^2 x B^2) f(x1,x2) g(x3,x4) d[alpha^(4) - alpha^(2) tensor alpha^(2)].`

Thus the covariance between quadratic pair statistics in disjoint source windows is a genuinely four-level functional relative to the `12|34` pair factorization. The one- and two-level laws, and even all three-level inclusion marginals, do not determine it in general.

An explicit four-site matched control proves the identifiability failure. Independent Bernoulli-`1/2` occupancy and uniform even-parity occupancy on four sites have identical inclusion probabilities for every subset of at most three sites, but for the disjoint pair indicators `F=X1 X2` and `G=X3 X4` their covariances are respectively `0` and `1/16`.

**Evidence/status:** `EXACT-DERIVED + MATCHED-THREE-LEVEL CONTROL + NEGATIVE IDENTIFIABILITY RESULT + CLASSICAL POINT-PROCESS/U-STATISTIC INGREDIENTS + NO-NOVELTY-CLAIM`.

The result does not estimate any zeta four-level correlation and does not claim that the actual zeta source-window process has the parity dependence used in the control.

## 1. Exact factorial-moment expansion

Write `f_12=f(x1,x2)` and similarly for `g`. In the product `U_f U_g`, the two ordered pairs may contain four, three, or two distinct points. The factorial-moment Campbell expansion gives

`E[U_f U_g]`

`= integral f_12 g_34 d alpha^(4)`

`+ integral f_12 [g_13 + g_31 + g_23 + g_32] d alpha^(3)`

`+ integral f_12 [g_12 + g_21] d alpha^(2).`

The four third-order terms are the four possible ways for exactly one endpoint of the `g` pair to coincide with one endpoint of the `f` pair. The two second-order terms are the two possible orientations when both pairs use the same two points. Separately,

`E[U_f] E[U_g] = (integral f d alpha^(2))(integral g d alpha^(2)).`

This is a standard order-two U-statistic/factorial-moment decomposition; the Mathia use here is only to identify exactly which correlation order controls the cross-window covariance gate left open by `VIS-136`--`VIS-138`.

## 2. Disjoint source windows remove all lower-order contractions

Suppose `supp(f) subset A x A` and `supp(g) subset B x B` with `A intersect B = emptyset`. Every three-point term requires one point to belong simultaneously to `A` and `B`, so it vanishes. The two-point terms vanish for the same reason. Therefore

`E[U_f U_g] = integral_(A^2 x B^2) f_12 g_34 d alpha^(4)`.

Subtracting the product of expectations yields the claimed formula. This should not be called the full fourth factorial cumulant: it is the four-level contribution after subtracting the particular independent-pair block `alpha^(2) tensor alpha^(2)`. That distinction matters because other lower-order partitions may still be encoded inside `alpha^(4)` for a general process.

For the support-edge program, the consequence is nevertheless sharp. Once two source windows are disjoint and each frozen statistic is quadratic in its local point configuration, the cross-window covariance cannot be inferred from the two-point pair-correlation law alone unless some additional structural theorem closes the four-level term.

## 3. A matched three-level control with different covariance

Take four fixed sites and occupancy variables `X_1,...,X_4`.

**Model I:** the four bits are independent Bernoulli `1/2`.

**Model P:** choose uniformly among the eight bit strings satisfying

`X_1 xor X_2 xor X_3 xor X_4 = 0`.

The even-parity model is three-wise independent. For any specified set of `r<=3` distinct sites and any assignment of their bits, exactly `2^(3-r)` even-parity completions remain, so the joint probability is `2^-r`, exactly as in Model I. In particular the two point processes have identical factorial inclusion data through order three.

Now put

`F = X_1 X_2`, `G = X_3 X_4`.

These are pair statistics on disjoint two-site windows; equivalently, they are order-two U-statistics obtained by assigning weight `1/2` to each orientation of the relevant site pair. In both models

`E[F]=E[G]=1/4`.

For Model I,

`E[FG]=1/16`, hence `Cov(F,G)=0`.

For Model P, the all-one configuration is one of the eight admissible even-parity states, so

`E[FG]=1/8`, hence `Cov(F,G)=1/8-1/16=1/16`.

Thus matching every one-, two-, and three-level inclusion marginal still leaves the covariance of disjoint quadratic pair statistics unidentified. The missing information enters first at level four in this control.

## 4. Consequence for the Montgomery support-edge experiment

`VIS-133` identifies the frozen bounded-tent support-edge observable as an intensity/quadratic functional of the local spectral configuration, while `VIS-136` shows that the cross-source-window covariance tail fixes the averaging exponent needed to resolve a shrinking `1/L` signal. `VIS-138` already proves that exact one-window CUE marginals do not determine that tail.

The present result isolates a stricter mathematical boundary: **Montgomery-style two-level/pair-correlation information by itself cannot determine the covariance between disjoint quadratic source-window statistics.** Even supplementing it with arbitrary exact three-level marginal information is insufficient without a four-level relation or a structural closure theorem.

Therefore a zeta-side argument that tries to close the `VIS-136` averaging gate through pair correlation alone is underdetermined at the level of point-process identities. A successful route must provide at least one of the following mathematical ingredients: a four-level correlation estimate strong and uniform enough for the frozen pair kernel and `L`-dependent source-window family; a structural law such as an appropriate determinantal/Gaussian/Wick closure that rigorously reduces the needed four-level term to lower-order data in the relevant regime; or a direct covariance/mixing estimate that bypasses the factorial-moment expansion.

This does **not** say that the classical zeta `n`-level correlation machinery supplies the required bound automatically. Rudnick--Sarnak place higher `n`-level zero correlations in the correct classical language, but their support restrictions and asymptotic regime must be checked against the exact frozen bounded-tent kernel and moving source-window geometry before they can be used here.

## Prior-art and novelty assessment

Point-process factorial moment measures and Campbell expansions are classical. Order-`k` point-process U-statistics are standard objects; for a representative modern reference see Matthias Reitzner and Matthias Schulte, **Central limit theorems for U-statistics of Poisson point processes**, *Annals of Probability* 41:6 (2013), 3879--3909, DOI `10.1214/12-AOP817`.

Higher-level zero correlations are likewise classical in analytic number theory and random-matrix comparisons. A central reference is Zeév Rudnick and Peter Sarnak, **Zeros of principal L-functions and random matrix theory**, *Duke Mathematical Journal* 81:2 (1996), 269--322, DOI `10.1215/S0012-7094-96-08115-6`.

No novelty is claimed for the general factorial-moment expansion, the existence of higher-level correlation theory, or parity examples of finite `k`-wise independence. The durable Mathia contribution is the exact specialization of these standard ingredients to the current support-edge feasibility question, together with an explicit matched-through-order-three control proving that lower-order calibration cannot identify the cross-window covariance needed by the active experiment.

## Boundaries

This finding is an information-order obstruction, not a zeta covariance theorem. It does not establish stationarity, mixing, decay, or non-decay across actual zeta height windows. It does not determine the sign or scale of the four-level connected pair-block term. It also does not show that four-level information is always necessary when additional structure is present: a valid closure theorem may derive it from lower-order objects.

The disjoint-support reduction applies only when the two source kernels genuinely have disjoint point support. Overlapping source windows reintroduce the explicit second- and third-order contraction terms in the general expansion and must be treated separately.

## Research consequence

The accepted clue `CLUE-zeta-montgomery-support-edge-arithmetic-residual` should no longer ask vaguely for an unspecified multi-window coupling. Its next gate can be sharpened to a concrete information-order question: derive the four-level cross-height functional for the exact frozen zeta pair statistic, prove a structural closure that controls it uniformly in `L`, or bypass it with a direct covariance/mixing theorem. Until one of those routes succeeds, two-level Montgomery calibration cannot justify the averaging exponent.