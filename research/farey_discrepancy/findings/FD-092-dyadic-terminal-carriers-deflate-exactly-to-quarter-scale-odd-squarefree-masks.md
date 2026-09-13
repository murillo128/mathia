# FD-092 — dyadic terminal carriers deflate exactly to quarter-scale odd-squarefree masks

**Status:** `EXACT-DERIVED + DYADIC-CHANNEL-DECOMPOSITION + QUARTER-SCALE-DEFLATION + ODD-SQUAREFREE-TERMINAL-MASK + UNIVERSAL-REEMBEDDING-MINIMALITY + FALSE-RH-FRONTIER + RECURSION-FRONTIER`.

`FD-091` reduces the recursively eligible predecessor problem to two branches. Odd repeated primes admit an exact square reembedding to a genuinely lower nonsquarefree state, while the dyadic reembedding by the smallest universal square multiplier is scale-critical. The latter statement leaves the dyadic branch looking like one indivisible obstruction.

It is not indivisible. At the canonical dyadic predecessor

\[
A:=A_2=\left\lceil\frac H2\right\rceil,
\]

split the selected lower rows according to whether they are already nonsquarefree. Every selected dyadic lower row has the form `s=2t`, because its parent row is `r=2s` with `4\mid r`. Hence either `s` is already nonsquarefree, in which case the transported energy is immediately recursively eligible at the genuine half-scale state `A`, or `s` is squarefree. In the latter case necessarily

\[
s=2m,
\qquad m\text{ odd and squarefree},
\qquad r=4m.
\]

That terminal piece has a second exact deflation. Put

\[
B:=\left\lfloor\frac A2\right\rfloor.
\]

Then for every such `s=2m`,

\[
\left\lfloor\frac{A}{2m}\right\rfloor
=
\left\lfloor\frac{B}{m}\right\rfloor,
\]

while the Jordan weight satisfies

\[
w(2m)=\frac34\,w(m).
\]

Therefore the entire terminal dyadic mask is exactly `3/4` of a genuine physical energy mask at the quarter-scale predecessor `B=H/4+O(1)`, supported **only on odd squarefree rows**. There is no source approximation and no rowwise horizon error in this second deflation.

Combining this identity with the dyadic/odd split of `FD-091` gives a sharper three-way frontier. On every sufficiently sharp occupied false-RH seed, either the odd-prime branch supplies the already-known lower nonsquarefree carrier, or the dyadic half-scale state contains a fixed raw amount of nonsquarefree energy, or a genuine quarter-scale state contains a fixed raw amount of energy on an adaptive odd-squarefree mask. Thus the unresolved dyadic obstruction is not generic `p=2` transport: it is precisely an **adaptive squarefree-sector carrier**.

There is also an exact minimality statement. Starting from an arbitrary odd-squarefree terminal row `m` at scale `B`, any fixed universal dilation `m\mapsto dm` that forces the image to be nonsquarefree for every possible terminal mask must have `d` itself nonsquarefree. Hence `d\ge4`. Exact quotient preservation then uses horizon `dB`, and the smallest choice obeys

\[
4B=H+O(1).
\]

So no universal fixed dilation can turn the terminal mask back into a nonsquarefree carrier while retaining a fixed-factor descent. Any further progress through this channel must exploit arithmetic structure of the **actual adaptive squarefree mask** (for example common factors or source-specific coherence), a non-universal row-dependent transport, or a genuinely different composition mechanism.

## 1. Setup and the exact dyadic split

Use the notation of `FD-089`--`FD-091`. On a sharp occupied block let

\[
M_{2,H}
:=
\|P_{S_{2,H}}V_{A,1}\|_2^2,
\qquad
A=\left\lceil\frac H2\right\rceil.
\tag{1}
\]

The deterministic repeated-prime assignment of `FD-089` assigns a parent row `r` to `p=2` only through a square divisibility `4\mid r`. Repeated-prime deflation writes

\[
r=2s,
\qquad 2\mid s,
\tag{2}
\]

and preserves the Jordan weight,

\[
w(r)=w(s).
\tag{3}
\]

Partition the selected lower support into

\[
S_{2,H}^{\rm elig}
:=
\{s\in S_{2,H}:\mu(s)=0\},
\qquad
S_{2,H}^{\rm term}
:=
\{s\in S_{2,H}:\mu(s)\ne0\},
\tag{4}
\]

with corresponding energies

\[
M_{2,H}^{\rm elig}
:=
\|P_{S_{2,H}^{\rm elig}}V_{A,1}\|_2^2,
\qquad
M_{2,H}^{\rm term}
:=
\|P_{S_{2,H}^{\rm term}}V_{A,1}\|_2^2.
\tag{5}
\]

The supports are disjoint, so exactly

\[
\boxed{
M_{2,H}=M_{2,H}^{\rm elig}+M_{2,H}^{\rm term}.
}
\tag{6}
\]

The first part is already a recursively eligible physical mask: every row in `S_(2,H)^elig` is nonsquarefree. Therefore

\[
\boxed{
M_{2,H}^{\rm elig}\le U_{A,1}.
}
\tag{7}
\]

The complement has a rigid arithmetic form. If `s\in S_(2,H)^term`, then `2\mid s` by (2) and `s` is squarefree by definition. Consequently there is a unique odd squarefree integer `m` such that

\[
\boxed{
s=2m,
\qquad r=4m,
\qquad m\text{ odd squarefree}.
}
\tag{8}
\]

Conversely, a selected dyadic parent of the form `r=4m` with `m` odd squarefree deflates to the terminal row `s=2m`. Thus (8) is an exact classification, not merely a sufficient condition. In particular, dyadic parents with `8\mid r` or with an odd squared prime factor are **not** terminal: after one dyadic deflation their lower row remains nonsquarefree and belongs to (7).

## 2. The terminal piece has an exact quarter-scale physical representation

Define

\[
B:=\left\lfloor\frac A2\right\rfloor
=
\left\lfloor\frac12\left\lceil\frac H2\right\rceil\right\rfloor
=\frac H4+O(1),
\tag{9}
\]

and let

\[
T_H
:=
\{m:\ 2m\in S_{2,H}^{\rm term}\}.
\tag{10}
\]

Every `m\in T_H` is odd and squarefree. The quotient map is exact because floor composition by integer divisors gives

\[
\boxed{
\left\lfloor\frac A{2m}\right\rfloor
=
\left\lfloor
\frac{\lfloor A/2\rfloor}{m}
\right\rfloor
=
\left\lfloor\frac Bm\right\rfloor.
}
\tag{11}
\]

For the Jordan weight

\[
w(n)=\frac{J_2(n)}{n^2}
=\prod_{p\mid n}(1-p^{-2}),
\tag{12}
\]

oddness of `m` gives

\[
\boxed{
w(2m)=\left(1-2^{-2}\right)w(m)=\frac34w(m).}
\tag{13}
\]

Using (11)--(13) in the terminal part of (5),

\[
\begin{aligned}
M_{2,H}^{\rm term}
&=
\sum_{m\in T_H}
w(2m)
\mathcal H\!\left(\left\lfloor\frac A{2m}\right\rfloor\right)^2\\
&=
\frac34
\sum_{m\in T_H}
w(m)
\mathcal H\!\left(\left\lfloor\frac Bm\right\rfloor\right)^2.
\end{aligned}
\tag{14}
\]

Hence, with the genuine physical quarter-scale mask energy

\[
Q_{B,H}
:=
\|P_{T_H}V_{B,1}\|_2^2,
\tag{15}
\]

one has the exact identity

\[
\boxed{
Q_{B,H}=\frac43M_{2,H}^{\rm term},
\qquad
T_H\subset\{m:\ m\text{ odd squarefree}\}.
}
\tag{16}
\]

There is no `O(1)` source displacement in (16), no use of the one-step Lipschitz bound for `mathcal H`, and no row-adaptive horizon. The only distortion is the explicit fixed Jordan factor `4/3`.

This also shows why the terminal obstruction differs qualitatively from the odd-prime branch of `FD-091`: after two exact dyadic deflations the scale really has descended by a factor four, but the repeated-prime witness has been completely consumed. What remains is a squarefree physical carrier.

## 3. Occupied frontier blocks satisfy a three-way lower-scale alternative

Retain an occupation level `eta>0` from `FD-084`--`FD-091`. The dyadic/odd split in `FD-091` says that, after the same vanishing Hilbert errors are absorbed, either the odd-prime channels carry at least `(eta/2-o(1))E_(H,1)`, or

\[
M_{2,H}\ge\frac\eta2E_{H,1}.
\tag{17}
\]

In the odd case, `FD-091` already gives the exact odd-square reembedding to lower horizons

\[
C_p=4\left\lfloor\frac{A_p}{p}\right\rfloor
=\frac{4H}{p^2}+O(1)
\le\frac49H+O(1),
\qquad p\ge3,
\tag{18}
\]

with nonsquarefree support and no predecessor-count entropy loss after the `p^{-4\sigma}` normalization.

Suppose instead that (17) holds. By (6), at least one of its two pieces carries half of that energy. If

\[
M_{2,H}^{\rm elig}\ge\frac12M_{2,H},
\]

then (7) gives

\[
\boxed{
U_{A,1}
\ge
\frac\eta4E_{H,1},
\qquad
A=\frac H2+O(1).
}
\tag{19}
\]

If the terminal piece carries at least half, then (16) gives

\[
\boxed{
Q_{B,H}
\ge
\frac\eta3E_{H,1},
\qquad
B=\frac H4+O(1),
\qquad
T_H\text{ odd squarefree}.
}
\tag{20}
\]

Thus the live frontier is the following trichotomy:

1. an odd repeated prime yields a genuinely lower nonsquarefree carrier as in `FD-091`;
2. the dyadic branch is already nonsquarefree at the genuine half-scale predecessor and (19) restores recursive eligibility directly;
3. the only genuinely terminal dyadic branch becomes the quarter-scale odd-squarefree physical mask (20).

The last alternative also preserves the false-RH frontier exponent. If the occupied seed is chosen with

\[
E_{H,1}>H^{2\Theta-\kappa},
\tag{21}
\]

then (20) and `B=H/4+O(1)` give

\[
Q_{B,H}\gg_{\eta,\Theta}B^{2\Theta-\kappa}.
\tag{22}
\]

On the other hand, the zero-frontier pointwise bound `FD-046` implies for every fixed `\sigma>\Theta`

\[
E_{B,1}
\ll_\sigma
B^{2\sigma}
\sum_{m\ge1}m^{-2\sigma}
\ll_\sigma B^{2\sigma}.
\tag{23}
\]

Since `Q_(B,H)<=E_(B,1)`, diagonalizing `kappa\downarrow0` and `sigma\downarrow\Theta` shows that in alternative (3)

\[
\boxed{
Q_{B,H}=B^{2\Theta-o(1)}
\quad\text{and}\quad
E_{B,1}=B^{2\Theta-o(1)}
}
\tag{24}
\]

in the usual frontier-exponent sense. The dyadic terminal route therefore does not lose the energy exponent; it loses **recursive nonsquarefree eligibility** and nothing else.

## 4. Universal exact reembedding cannot restore eligibility below the parent scale

Could one repeat the `FD-091` square-reembedding trick after (16)? Suppose one tries to replace every possible terminal row `m` by `dm` for a fixed positive integer `d`, and simultaneously replaces the horizon `B` by

\[
C=dB.
\tag{25}
\]

Then quotient preservation is exact:

\[
\left\lfloor\frac{C}{dm}\right\rfloor
=
\left\lfloor\frac Bm\right\rfloor.
\tag{26}
\]

To force `dm` to be nonsquarefree for **every possible odd-squarefree terminal row** `m`, however, `d` itself must be nonsquarefree. Indeed, if `d` were squarefree, choose an odd squarefree `m` coprime to `d` (for instance an odd prime outside the finite support of `d`); then `dm` would remain squarefree. Therefore

\[
\boxed{d\text{ universal and eligibility-forcing}\Longrightarrow d\ge4.}
\tag{27}
\]

The smallest possible universal choice is `d=4`. From (9), a direct residue-class check gives

\[
4B\in\{H-2,H-1,H,H+1\},
\tag{28}
\]

so in particular

\[
\boxed{4B=H+O(1).}
\tag{29}
\]

Thus every universal exact multiplicative repair of the terminal squarefree mask is scale-critical: it returns to the parent scale up to a bounded error. No choice can give

\[
C\le(1-\varepsilon)H
\]

for any fixed `\varepsilon>0` once `H` is large.

This is a universal statement, not a claim about every **actual** terminal mask. If a specific adaptive mask has extra common-factor structure, a smaller `d` may make all of its rows nonsquarefree; for example a mask supported entirely on multiples of an odd prime can exploit that prime. Likewise, row-dependent multipliers are not excluded. Both possibilities are source-specific information absent from the generic carrier geometry and are exactly the kind of additional structure a successful continuation would now have to prove.

## 5. Stress tests and boundary cases

The floor identity (11) is insensitive to the parity of `H`; it is the elementary identity `floor(floor(A/2)/m)=floor(A/(2m))` for integers `A,m>=1`. The only parity effect is the bounded residue in (28), so no asymptotic scale claim depends on choosing even horizons.

The classification (8) also handles all square divisibility correctly. If the parent contains `2^3`, then the lower row contains `2^2` and belongs to the eligible half-scale part. If the parent has exact `2`-adic valuation two but its odd part contains `q^2`, then that `q^2` survives the dyadic deflation and again puts the lower row in the eligible part. Hence the terminal class really is exactly `4m` with `m` odd squarefree.

The factor `4/3` in (16) is exact because `w(n)` depends only on the radical of `n`: adding the prime `2` to an odd support multiplies `w` by `1-2^{-2}=3/4`, while changing the exponent of an already present prime would not change it. No sign information is used, because the physical energy is quadratic.

Finally, (24) is only an exponent statement. It does **not** show that the adaptive terminal mask occupies a fixed fraction of the quarter-scale energy `E_(B,1)`; the ratio can still be `B^{-o(1)}`. Nor does squarefree support by itself give the desired GCD/Schur accumulation. `FD-032` in fact shows that squarefree support is precisely where the unrestricted equality direction lives, so the terminal branch has moved into the structurally most saturation-compatible sector rather than into an obviously forbidden one.

## 6. Prior-art boundary and new frontier

A nearby external result is William D. Banks, *On the distribution of reduced fractions with squarefree denominators*, Acta Arithmetica 206 (2022), 1--34, DOI `10.4064/aa210905-20-9`. Banks studies the **complete** family of Farey fractions with squarefree denominators and relates quantitative discrepancy bounds for that family to zero-free regions of `zeta(s)`. That result does not control (20): `T_H` is an adaptive subset selected by the source energy and the repeated-prime carrier, and its Jordan-weighted quotient-shell energy need not resemble the complete squarefree-denominator family. It is therefore useful prior art but not a load-bearing input here; `SOURCES.md` does not need a new dependency.

The frontier after `FD-092` is sharper than the generic dyadic obstruction left by `FD-091`. The unresolved channel is now:

\[
\boxed{
\text{frontier-sized energy on an adaptive odd-squarefree mask at }B\sim H/4.
}
\tag{30}
\]

A successful next step must either prove that this adaptive mask has enough extra arithmetic structure to admit a smaller non-universal reembedding, show that its projective position is incompatible with repeated near-saturation of the GCD/Schur duality, or couple it to the complete squarefree-denominator discrepancy in a way strong enough to survive adaptive support selection. Merely applying another universal square multiplier cannot create a descending recurrence.