# RE-169 — Mertens normalization turns post-selector ambiguity into remote compensation debt

**Status:** `EXACT-DERIVED + MERTENS-NORMALIZATION-FIDELITY + MATCHED-SOURCE-SUM-RULE + KV-TAIL-COMPENSATION + GENERALIZED-CONTROL-BOUNDARY + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-008, RE-153, RE-154, RE-164, RE-166, RE-167, RE-168.

`RE-154` and `RE-167`--`RE-168` show that a source can be changed after a fixed CA selector by an asymptotically tiny amount, remain PNT- or even Korobov--Vinogradov-faithful, and still move the normalized `RE-153` Robin source coordinate by order one. Those controls deliberately preserve the Chebyshev envelope, but they do **not** preserve the logarithmic Mertens-product normalization at the precision seen by the Robin kernel.

There is an exact global sum rule. For a prime-like source `Q`, put

\[
\Gamma(Q)
:=
\lim_{x\to\infty}
\left(
\int_{2^-}^{x} h(t)\,d\vartheta_Q(t)
-
\log\log x
\right),
\qquad
h(t):=\frac{-\log(1-t^{-1})}{\log t},
\tag{1}
\]

whenever the limit exists. For the ordinary primes, classical Mertens gives

\[
\Gamma(P)=\gamma.
\tag{2}
\]

Let two sources `Q_1,Q_2` agree below a cutoff `T`, assume

\[
\vartheta_{Q_i}(t)=t+o(t),
\tag{3}
\]

and assume both constants in (1) exist. Write

\[
F(t):=\vartheta_{Q_2}(t)-\vartheta_{Q_1}(t).
\tag{4}
\]

Then

\[
\boxed{
\Gamma(Q_2)-\Gamma(Q_1)
=
\int_T^\infty F(t)(-h'(t))\,dt.
}
\tag{5}
\]

Consequently, if

\[
\mathcal A_{p,U}(Q)
:=
\frac{\sqrt p\log p}{Z_p}
\int_{p+p^\alpha}^{U}
\bigl(t-\vartheta_Q(t)\bigr)(-h'(t))\,dt,
\qquad Z_p=2+o(1),
\tag{6}
\]

and `T>=p+p^alpha`, then for every `U>=T`

\[
\boxed{
\mathcal A_{p,U}(Q_1)-\mathcal A_{p,U}(Q_2)
=
\frac{\sqrt p\log p}{Z_p}
\bigl(\Gamma(Q_2)-\Gamma(Q_1)\bigr)
-
\frac{\sqrt p\log p}{Z_p}
\int_U^\infty F(t)(-h'(t))\,dt.
}
\tag{7}
\]

Thus the middle-annulus ambiguity is not free once the global Mertens normalization is part of the fidelity class. If `Gamma(Q_1)=Gamma(Q_2)`, every accumulated post-selector Robin displacement is an exact **debt to the still-unseen tail**.

If, moreover, both sources satisfy for `t>=U`

\[
|\vartheta_{Q_i}(t)-t|
\le C_i t e^{-bV(t)},
\qquad
V(t):=\frac{(\log t)^{3/5}}{(\log\log t)^{1/5}},
\tag{8}
\]

then the debt law becomes

\[
\boxed{
\left|
\mathcal A_{p,U}(Q_1)-\mathcal A_{p,U}(Q_2)
-
\frac{\sqrt p\log p}{Z_p}
\bigl(\Gamma(Q_2)-\Gamma(Q_1)\bigr)
\right|
\ll_{C_1,C_2,b}
\mathfrak K_b(p,U),
}
\tag{9}
\]

where

\[
\mathfrak K_b(p,U)
:=
\sqrt p\log p\,
\frac{e^{-bV(U)}}{V(U)}
\tag{10}
\]

is exactly the remote-tail capacity of `RE-165`--`RE-166`. In particular,

\[
\boxed{
\Gamma(Q_1)=\Gamma(Q_2),
\qquad
\mathfrak K_b(p,U)=o(1)
\quad\Longrightarrow\quad
\mathcal A_{p,U}(Q_1)-\mathcal A_{p,U}(Q_2)=o(1),
}
\tag{11}
\]

**without any pointwise source control at all on the intervening interval `[T,U]`.**

The `RE-154`/`RE-167` local controls therefore expose a more precise information boundary than previously recorded. A compact mass-balanced relocation with nonzero normalized Robin displacement necessarily changes the Mertens normalization by exactly the critical amount

\[
\boxed{
|\Gamma(Q_2)-\Gamma(Q_1)|
=
\frac{Z_p}{\sqrt p\log p}
\left|
\mathcal A_p(Q_1)-\mathcal A_p(Q_2)
\right|.
}
\tag{12}
\]

Hence order-one Robin ambiguity costs only `Theta((sqrt(p) log p)^(-1))` in the Mertens constant. Qualitative Mertens fidelity, `Gamma(Q_p)=gamma+o(1)`, still does not detect the controls. But fidelity at the sharper scale

\[
\boxed{
|\Gamma(Q_p)-\gamma|
=o\!\left(\frac1{\sqrt p\log p}\right)
}
\tag{13}
\]

combined with a KV-rigid upper tail does.

This materially changes the generalized-source frontier. Quantitative PNT fidelity alone leaves the bounded-multiplicative ambiguity of `RE-167`; adding the correct Mertens normalization converts every such local shift into a compulsory later cancellation. That cancellation cannot be postponed beyond the moving `RE-166` capacity center by more than `O(1)` in the `V` coordinate while carrying a fixed nonzero debt.

## 1. Exact Mertens sum rule

Because the two sources agree below `T`, equation (4) satisfies

\[
F(T^-)=0.
\tag{14}
\]

For finite `X>T`, Stieltjes integration by parts gives

\[
\int_T^X h(t)\,dF(t)
=
h(X)F(X)
+
\int_T^X F(t)(-h'(t))\,dt.
\tag{15}
\]

The PNT-scale hypothesis (3), together with

\[
h(X)\sim\frac1{X\log X},
\tag{16}
\]

implies

\[
h(X)F(X)\longrightarrow0.
\tag{17}
\]

On the other hand, subtracting the two limits in (1) cancels `log log X` and yields

\[
\Gamma(Q_2)-\Gamma(Q_1)
=
\lim_{X\to\infty}
\int_T^X h(t)\,dF(t).
\tag{18}
\]

Equations (15)--(18) prove (5). No zero-density estimate, RH hypothesis, or generalized-prime Mertens theorem is needed once existence of the two constants is assumed.

For the finite modifications used in `RE-154` and `RE-167`--`RE-168`, existence is automatic: after the last modified label, the generalized Euler product differs from the ordinary one by one fixed finite factor. Thus those controls have an exactly defined `Gamma(Q)` even though it need not equal `gamma`.

## 2. The Robin coordinate is the truncated part of the same global invariant

Taking the difference of (6) eliminates the deterministic `t` term. Since the sources agree below `T`,

\[
\mathcal A_{p,U}(Q_1)-\mathcal A_{p,U}(Q_2)
=
\frac{\sqrt p\log p}{Z_p}
\int_T^U F(t)(-h'(t))\,dt.
\tag{19}
\]

Split the global identity (5) at `U`:

\[
\int_T^U F(-h')
=
\Gamma(Q_2)-\Gamma(Q_1)
-
\int_U^\infty F(-h').
\tag{20}
\]

Substitution into (19) proves (7).

Equation (20) is the source-fidelity statement that was absent from the coarse generalized controls. The same kernel `-h'` that measures the `RE-153` source coordinate also measures how a finite source surgery changes the asymptotic logarithmic Mertens product. There is no independent degree of freedom between those two quantities.

For equal Mertens constants, define the accumulated normalized debt

\[
D_p(U)
:=
\frac{\sqrt p\log p}{Z_p}
\int_T^U F(t)(-h'(t))\,dt.
\tag{21}
\]

Then (20) becomes the exact conservation law

\[
\boxed{
D_p(U)
=
-
\frac{\sqrt p\log p}{Z_p}
\int_U^\infty F(t)(-h'(t))\,dt.
}
\tag{22}
\]

So an early positive displacement cannot disappear by resetting the cumulative Chebyshev discrepancy to zero. If the source is required to recover the same global Mertens normalization, an equal negative weighted displacement must occur later.

## 3. KV fidelity caps how long the debt can survive

Under (8),

\[
|F(t)|
\le
(C_1+C_2)t e^{-bV(t)}.
\tag{23}
\]

The elementary derivative estimate already used in `RE-164`--`RE-168`,

\[
-h'(t)\ll\frac1{t^2\log t},
\tag{24}
\]

gives

\[
\begin{aligned}
\frac{\sqrt p\log p}{Z_p}
\int_U^\infty |F(t)|(-h'(t))\,dt
&\ll
\sqrt p\log p
\int_U^\infty
\frac{e^{-bV(t)}}{t\log t}\,dt\\
&\ll_b
\mathfrak K_b(p,U).
\end{aligned}
\tag{25}
\]

Together with (7), this proves (9)--(11).

There is also a useful dynamic form. If the constants agree and for some moving height `H=H(p)` the source has accumulated a fixed debt

\[
|D_p(H)|\ge\delta>0,
\tag{26}
\]

then necessarily

\[
\boxed{
\mathfrak K_b(p,H)\gg_{b,C_1,C_2}\delta.
}
\tag{27}
\]

Let `v_*(p)` be the `RE-166` remote capacity-one center,

\[
v_*(p)
=
\frac1b W_0\!\left(b\log p\sqrt p\right).
\tag{28}
\]

`RE-166` gives, for `Delta=V(H)-v_*(p)`,

\[
\mathfrak K_b(p,H)
=
\frac{e^{-b\Delta}}{1+\Delta/v_*(p)}.
\tag{29}
\]

Hence a fixed nonzero debt cannot persist into a region with

\[
V(H)-v_*(p)\longrightarrow+\infty.
\tag{30}
\]

More quantitatively, for fixed envelope constants and fixed `delta`, (27)--(29) force

\[
\boxed{
V(H)\le v_*(p)+O_{b,C_1,C_2,\delta}(1).
}
\tag{31}
\]

Thus Mertens-normalized source surgery may still create a local post-selector excursion, but it must repay that excursion no later than an `O(1)` neighborhood of the moving KV capacity center in the intrinsic `V` coordinate.

## 4. Audit of the existing generalized controls

Suppose a finite modification is supported in `[T,U_0]` and is exactly Chebyshev-mass balanced, so

\[
F(t)=0
\qquad(t\ge U_0).
\tag{32}
\]

Then (5) and (19), with any `U>=U_0`, give the exact identity

\[
\boxed{
\mathcal A_{p,U}(Q_1)-\mathcal A_{p,U}(Q_2)
=
\frac{\sqrt p\log p}{Z_p}
\bigl(\Gamma(Q_2)-\Gamma(Q_1)\bigr).
}
\tag{33}
\]

This applies directly to the balanced fixed-shell relocation of `RE-167` and to each concatenated balanced relocation in `RE-168`. Their order-one Robin leverage is therefore exactly an order `1/(sqrt(p) log p)` shift of the asymptotic Mertens normalization.

This does **not** invalidate those findings. Their stated fidelity class is PNT/Chebyshev fidelity, and within that class their sharpness claims remain correct. It does, however, prevent using them as controls against an argument that additionally exploits the ordinary source's Mertens normalization at the critical precision.

The precision qualifier is essential. If a compact control has

\[
\mathcal A_{p,U}(Q)-\mathcal A_{p,U}(P)\to\Delta\ne0,
\tag{34}
\]

then (33) and `Z_p=2+o(1)` give

\[
\Gamma(Q)-\gamma
=
\Theta\!\left(\frac1{\sqrt p\log p}\right)
\longrightarrow0.
\tag{35}
\]

So every such moving family still satisfies the qualitative statement

\[
\Gamma(Q_p)=\gamma+o(1).
\tag{36}
\]

Merely appending a qualitative Mertens theorem to the generalized-source fidelity class changes nothing. The source must be matched to the finer scale (13), or exactly, before the new rigidity enters.

## 5. Falsification checks and scope

**Could a later compensation restore the constant?** Yes. Equation (22) explicitly allows it. This is why exact Mertens matching does not forbid a local relocation in isolation; it converts it into a later opposite-sign debt. The new statement is that a KV-faithful source cannot postpone a fixed debt beyond the remote capacity center.

**Could compensation be hidden arbitrarily far above the `RE-153` horizon?** Not while retaining the same fixed KV exponent and constants once the tail capacity is `o(1)`. Equation (25) bounds the entire remaining weighted compensation, independent of how it is distributed.

**Does the ordinary value `Gamma(P)=gamma` prove Robin?** No. For the ordinary source, Mertens normalization is a global identity and does not by itself bound the selected finite-prefix Mertens error `E(p)` or the endpoint-subtracted remainder of `RE-008`. It says that every finite-prefix excursion has a compensating future weighted history; the unresolved CA problem is to control that history at the selector-selected primes. Using `Gamma(P)=gamma` without an independent selected-prefix estimate would simply recycle the exact Mertens identity.

**Does PNT imply the generalized constant used here?** This finding does not assume that. It requires existence of `Gamma(Q)` explicitly. For the finite modifications that matter to the audit of `RE-154` and `RE-167`--`RE-168`, existence follows immediately from the ordinary Mertens product and finite modification.

A targeted prior-art audit found the classical generalized Mertens literature, in particular Paul Pollack, *On Mertens' Theorem for Beurling Primes*, Canadian Mathematical Bulletin **56** (2013), 829--843, DOI `10.4153/CMB-2012-004-8`, which relates a Beurling zeta residue `A` at `s=1` to the product asymptotic `A e^gamma log x`. That literature confirms that generalized Mertens normalization is genuine source data rather than a consequence of bare prime density. It does not state the Robin-kernel sum rule (7), the critical precision (13), or the KV compensation law (27)--(31). No generalized-Mertens theorem is load-bearing in the derivation above, so `SOURCES.md` does not require a new anchor.

## 6. Research consequence

The source-side obstruction after `RE-168` needs one qualification. The ordinary source is not characterized only by its quantitative Chebyshev envelope; it also has a fixed logarithmic Mertens normalization. For matched controls, that single scalar is seen by the **same positive kernel** as the normalized Robin source.

Therefore a generalized-source falsification of selector-to-height coupling must now pass three fidelity tests simultaneously:

1. preserve the selector/prefix data;
2. preserve the quantitative PNT envelope;
3. preserve `Gamma` to `o((sqrt(p) log p)^(-1))`, or explicitly exhibit where the compensating Mertens debt is paid before the KV tail becomes rigid.

The existing bounded-multiplicative relocations pass the first two but not the third. The accepted `clean-peak-selector-height-coupling` clue remains open: the ordinary-prime task is still to control the selected endpoint-subtracted Mertens excursion, not merely to quote `Gamma(P)=gamma`. But the information-theoretic frontier is narrower than after `RE-168`: **post-selector Chebyshev mobility and Robin-height mobility are no longer independent once Mertens normalization is enforced at the target scale.**

**Provenance:** derived against default-branch snapshot `4166af4e5392791e84af6b7b92745458c4f10546`; stable finding prefix `RE`; no clue-state, `mind/**`, README, graph, or source-registry mutation required.