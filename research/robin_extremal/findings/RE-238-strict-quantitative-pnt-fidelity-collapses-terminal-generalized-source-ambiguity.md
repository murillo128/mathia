# RE-238 — Strict quantitative PNT fidelity collapses terminal generalized-source ambiguity

**Status:** `LITERATURE+DERIVED + QUANTITATIVE-PNT-FIDELITY + MATCHED-SOURCE-RIGIDITY + STRICT-THRESHOLD + CRITICAL-EQUALITY-OPEN + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-015, RE-153, RE-155, RE-157, RE-162, RE-163.

The terminal generalized-source controls of `RE-155`--`RE-163` can move the normalized Robin source coordinate by order one while remaining invisible to **coarse** prime-number-theorem information such as (artheta_Q(x)=x+o(x)). They do not, however, remain invisible once the comparison class is required to satisfy a sufficiently strong quantitative Korobov--Vinogradov-scale Chebyshev remainder.

The exact conclusion has a **strict** threshold. If two sources agree below a cutoff (T) and both satisfy
[
|artheta_Q(t)-t|ll t e^{-bV(t)},
qquad
V(t):=rac{(log t)^{3/5}}{(loglog t)^{1/5}},
]
then at the canonical Robin horizon (U_A(p)) the terminal contribution is (o(1)) whenever
[
bkappa_A>rac12,
qquad
kappa_A=A^{3/5}left(rac35ight)^{1/5}.
]
At the boundary (bkappa_A=1/2), the current unconditional envelope and the canonical horizon do **not** imply (o(1)). A second-order expansion shows that the hidden subpower correction goes in the wrong direction for the stored upper bound. The equality case therefore remains open.

Retain
[
U:=U_A(p),qquad
J_p=[p+p^alpha,U],qquad
h(t):=rac{-log(1-t^{-1})}{log t},
]
and the normalized source coordinate from `RE-153`,
[
mathcal A_p(Q)
:=
int_{J_p}
rac{t-artheta_Q(t)}{sqrt t},d
u_p(t),
qquad

u_p(dt)=rac{sqrt plog p,sqrt t,(-h'(t))}{Z_p},dt,
qquad
Z_p=2+o(1).
	ag{1}
]

Let (Q_1,Q_2) be two prime-like sources whose Chebyshev functions agree below (T), where
[
p+p^alphale T<U.
	ag{2}
]
Then
[
oxed{
mathcal A_p(Q_1)-mathcal A_p(Q_2)
=
rac{sqrt plog p}{Z_p}
int_T^U
igl(artheta_{Q_2}(t)-artheta_{Q_1}(t)igr)(-h'(t)),dt.
}
	ag{3}
]

Define
[
M_{12}(T,U)
:=
sup_{Tle tle U}
rac{|artheta_{Q_1}(t)-artheta_{Q_2}(t)|}{t}.
	ag{4}
]
Since
[
-h'(t)
=
rac1{t(t-1)log t}
+
rac{-log(1-t^{-1})}{t(log t)^2},
	ag{5}
]
we have uniformly for large (T),
[
int_T^U t(-h'(t)),dt
le
(1+o(1))
lograc{log U}{log T}.
	ag{6}
]
Consequently
[
oxed{
|mathcal A_p(Q_1)-mathcal A_p(Q_2)|
ll
sqrt plog p,M_{12}(T,U)
lograc{log U}{log T}.
}
	ag{7}
]

For a terminal logarithmic shell
[
T=Ue^{-L},qquad 0<L=o(log U),
	ag{8}
]
put
[
eta_p:=rac{log U}{sqrt plog p}.
	ag{9}
]
Then
[
oxed{
|mathcal A_p(Q_1)-mathcal A_p(Q_2)|
ll
rac{L}{eta_p},M_{12}(Ue^{-L},U).
}
	ag{10}
]
Hence any source-coordinate separation bounded below by a fixed (Delta>0) forces
[
oxed{
M_{12}(Ue^{-L},U)
gg_Delta
rac{eta_p}{L}.
}
	ag{11}
]
This necessary excursion is independent of cardinality, moment order, or Chebyshev-mode cancellation.

## 1. Quantitative PNT fidelity gives a stronger matched-source bound

Assume that on ([T,U]),
[
|artheta_{Q_i}(t)-t|
le C_i t e^{-b_iV(t)},
qquad i=1,2,
	ag{12}
]
for fixed positive (b_i,C_i), and put
[
b:=min(b_1,b_2).
	ag{13}
]
Then
[
|artheta_{Q_1}(t)-artheta_{Q_2}(t)|
ll t e^{-bV(t)}.
	ag{14}
]
Using (3) and (5),
[
oxed{
|mathcal A_p(Q_1)-mathcal A_p(Q_2)|
ll
sqrt plog p
int_T^U
rac{e^{-bV(t)}}{tlog t},dt.
}
	ag{15}
]

Two useful consequences are
[
oxed{
|mathcal A_p(Q_1)-mathcal A_p(Q_2)|
ll
sqrt plog p,e^{-bV(T)}
lograc{log U}{log T}
}
	ag{16}
]
and, after extending the positive majorant to infinity and applying the same tail estimate used in `RE-015`,
[
oxed{
|mathcal A_p(Q_1)-mathcal A_p(Q_2)|
ll
sqrt plog p,
rac{e^{-bV(T)}}{V(T)}.
}
	ag{17}
]

The first form is sharper for a bounded terminal shell; the second is the robust remote-tail form.

## 2. The canonical horizon gives rigidity only above the strict threshold

For
[
U_A(p)
=
exp!left(
A(log p)^{5/3}(loglog p)^{1/3}
ight),
	ag{18}
]
write
[
kappa_A:=A^{3/5}left(rac35ight)^{1/5}.
	ag{19}
]
Then
[
V(U_A(p))
=
kappa_Alog p,(1+o(1)).
	ag{20}
]

Take (0<Lle L_0) fixed and (T=U_A(p)e^{-L}). Also
[
eta_p
=
A p^{-1/2}(log p)^{2/3}(loglog p)^{1/3}.
	ag{21}
]
Substituting in (16),
[
oxed{
|mathcal A_p(Q_1)-mathcal A_p(Q_2)|
ll_{L_0}
p^{1/2-bkappa_A+o(1)}
(log p)^{-2/3}(loglog p)^{-1/3}.
}
	ag{22}
]

Therefore
[
oxed{
bkappa_A>rac12
quadLongrightarrowquad
mathcal A_p(Q_1)-mathcal A_p(Q_2)=o(1)
}
	ag{23}
]
for every bounded terminal shell.

This strict inequality is exactly sufficient for the matched-source rigidity needed here and is consistent with the strict margin used in the `RE-015` remote-tail truncation.

### The critical equality is not controlled by the present estimate

The case (bkappa_A=1/2) cannot be recovered from the (p^{o(1)}) notation in (22). Let
[
x:=log p,qquad y:=loglog p.
]
For bounded (L),
[
log T
=
A x^{5/3}y^{1/3}-L.
]
A direct expansion of the same function (V) gives
[
oxed{
V(T)
=
kappa_A x
left(
1-rac{log y+3log A}{25y}
+O!left(rac{(log y)^2}{y^2}ight)
ight).
}
	ag{24}
]
The bounded displacement (L) contributes only below this displayed scale.

At the critical equality (bkappa_A=1/2),
[
oxed{
p^{1/2}e^{-bV(T)}
=
exp!left(
rac{x(log y+3log A)}{50y}
+
O!left(rac{x(log y)^2}{y^2}ight)
ight).
}
	ag{25}
]
Thus the local-shell upper bound supplied by (16) contains a positive subpower factor
[
exp!left(rac{xlog y}{50y}(1+o(1))ight)
]
which dominates every fixed polylogarithmic saving. In particular, (22) does not imply (o(1)) at equality.

This is a limitation of the current bound, not a counterexample. No source pair satisfying the critical envelope and maintaining an order-one terminal Robin displacement is constructed here. The exact boundary
[
bkappa_A=rac12
]
remains unresolved by this method.

More generally, if
[
T=U_B(p)
=
exp!left(
B(log p)^{5/3}(loglog p)^{1/3}
ight),
qquad B<A,
	ag{26}
]
then (17) gives
[
|mathcal A_p(Q_1)-mathcal A_p(Q_2)|
ll
p^{1/2-bkappa_B+o(1)}.
	ag{27}
]
Hence whenever
[
bkappa_B>rac12,
	ag{28}
]
all source freedom above (U_B(p)) is (o(1)) in the Robin coordinate among sources that agree below (U_B(p)) and retain the quantitative PNT envelope.

## 3. Consequence for the terminal matched controls

The terminal controls in `RE-155`--`RE-163` preserve only coarse PNT information while producing a nonvanishing change in the normalized Robin source coordinate. Equation (11) identifies the missing information: an order-one terminal change necessarily creates, somewhere in a shell of logarithmic width (L), a relative Chebyshev discrepancy of size at least
[
asymprac{eta_p}{L}.
	ag{29}
]

Once the quantitative PNT exponent **strictly** clears the (1/2) inversion threshold, the allowed Chebyshev remainder is too small to support such a terminal displacement. Exact matching of many raw moments, low Chebyshev modes, or kernel-weighted low-mode sums does not change this conclusion: if the final Robin source displacement remains order one, the positive kernel in (3) still forces the cumulative excursion (11).

The generalized-source constructions therefore remain valid coarse-information obstructions, but they are not source-faithful controls for the full unconditional PNT remainder beyond the strict inversion scale. At the critical equality, this finding makes no rigidity claim.

## 4. Prior-art boundary and scope

The load-bearing external input is the quantitative PNT remainder already anchored in `SOURCES.md` and used by `RE-015`; no new external theorem is needed for the strict matched-source implication. The second-order calculation above is an elementary expansion of the canonical horizon and the same Korobov--Vinogradov profile.

The general literature on Beurling prime systems studies PNTs with quantitative remainder, but (12) is an explicit fidelity hypothesis on the comparison source rather than a theorem asserted for arbitrary generalized primes. The line-specific content is the propagation of that fidelity through the exact Robin kernel and the identification of the strict terminal rigidity threshold.

This finding does **not** prove Robin's inequality, control the middle annulus below the PNT inversion scale, establish a selector-height coupling, or settle the critical equality (bkappa_A=1/2). It also does not invalidate the coarse generalized-source controls. Its conclusion is narrower and exact: **strictly above the inversion threshold, quantitative PNT fidelity removes order-one terminal source ambiguity; at equality, the present argument does not.**

## 5. Audit and falsification boundary

The decisive checks are:

1. verify the exact matched-source identity (3) and positivity of the kernel;
2. verify the bounded-shell reduction (16);
3. verify the expansion (24) directly from (V(t)=(log t)^{3/5}/(loglog t)^{1/5});
4. do not infer convergence at (bkappa_A=1/2) from a (p^{o(1)}) factor;
5. treat any future equality-case claim as requiring either a sharper source hypothesis, a sharper horizon/tail estimate with the correct second-order sign, or an explicit critical matched control.

These checks separate the robust strict-threshold rigidity mechanism from the unresolved critical layer.
