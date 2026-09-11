# FD-054 — off-critical shell spikes force a nonsquarefree additive twin above the zero-frontier row threshold

**Status:** `EXACT-DERIVED + SOURCE-SPECIFIC + ZERO-FRONTIER-SPIKE + MOVING-SQUAREFREE-ROW + ADDITIVE-NONSQUAREFREE-WITNESS + PRIMORIAL-CALIBRATION + QUADRATIC-OCCUPATION + NEGATIVE/ROUTE-RESTRICTION`.

`FD-053` shows that even a moving squarefree Jordan host, all the way to the square-root row boundary, can cancel a false-RH shell spike at the level of the exact **signed multiplicative ray** without sending a comparable signed response through nonsquarefree multiples of that host. That is a real obstruction to any argument based only on the one-dimensional dilation first moment.

The ambient quadratic occupation behaves differently. The bounded-increment mechanism already present in `FD-037`, when calibrated by the zero-frontier spikes of `FD-046`, shows that a sufficiently large squarefree host value cannot remain isolated from the nonsquarefree rows **additively adjacent to the host**.

Let

\[
w(r):=\frac{J_2(r)}{r^2},
\qquad
\mathcal H(N)=\sum_{n\le N}c(n),
\qquad
|c(n)|\le1,
\]

and for fixed `D>=1` let

\[
U_{H,D}
:=
\sum_{\substack{D<r\le H\\\mu(r)=0}}
w(r)
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)^2.
\]

For an integer `X` and a squarefree host `q>D`, set

\[
H=qX,
\qquad
q^*:=4\left\lceil\frac q4\right\rceil.
\]

Then `q^*` is nonsquarefree, `1<=q^*-q<=3`, and

\[
\boxed{
0\le
X-\left\lfloor\frac{H}{q^*}\right\rfloor
\le \frac{3X}{q}+1.
}
\tag{1}
\]

Consequently the exact one-Lipschitz law gives

\[
\boxed{
\left|
\mathcal H(X)
-
\mathcal H\!\left(\left\lfloor\frac{H}{q^*}\right\rfloor\right)
\right|
\le \frac{3X}{q}+1.
}
\tag{2}
\]

Hence along any sequence with

\[
\boxed{
\frac{q\,|\mathcal H(X)|}{X}\longrightarrow\infty,
}
\tag{3}
\]

the additive nonsquarefree witness carries the same value to first order:

\[
\mathcal H\!\left(\left\lfloor\frac{H}{q^*}\right\rfloor\right)
=
\mathcal H(X)+o(|\mathcal H(X)|).
\tag{4}
\]

Since every Jordan weight is at least `1/zeta(2)`, the single row `q^*` already forces

\[
\boxed{
U_{H,D}
\ge
\left(\frac1{\zeta(2)}-o(1)\right)
|\mathcal H(X)|^2.
}
\tag{5}
\]

If

\[
J_q(H):=w(q)|\mathcal H(X)|^2
\]

is the energy of the original squarefree host row, then `w(q)<=1`, so

\[
\boxed{
U_{H,D}
\ge
\left(\frac1{\zeta(2)}-o(1)\right)J_q(H).
}
\tag{6}
\]

Thus any squarefree host satisfying (3) automatically acquires a **comparable nonsquarefree quadratic twin**, even though the signed multiplicative ray through that host can self-cancel entirely inside its squarefree branch.

## 1. The local transference criterion

The proof of (1)--(6) is deliberately elementary because the important point is where it applies.

Since `q^*>=q`,

\[
\frac{H}{q^*}
=\frac{qX}{q^*}
\le X.
\]

Also

\[
X-\frac{H}{q^*}
=X\left(1-\frac q{q^*}\right)
=X\frac{q^*-q}{q^*}
\le\frac{3X}{q}.
\]

Taking the floor costs at most one and proves (1). The coefficient formula from `FD-033` gives `|Delta mathcal H(n)|<=1`, hence (2). Condition (3) makes the right side of (2) negligible compared with `|mathcal H(X)|`, proving (4).

The row `q^*` is divisible by four, hence is nonsquarefree. For all sufficiently large members of the sequence it lies in `(D,H]`, and therefore its Jordan energy is one positive summand of `U_(H,D)`. The uniform Euler-product bound

\[
\frac1{\zeta(2)}\le w(r)\le1
\]

then proves (5)--(6).

This local inequality is not claimed as a new replacement for `FD-037`: its bounded-distance squarefree/nonsquarefree pairing is exactly the mechanism already used there. The new content is the calibration of that mechanism against the later zero-frontier and moving-primorial results, which identifies precisely where the `FD-053` signed escape ceases to be relevant to quadratic occupation.

## 2. Zero-frontier spikes determine the moving-row threshold

Let

\[
\Theta
:=
\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\]

`FD-046` proves that the shell source has the same power frontier:

\[
\limsup_{X\to\infty}
\frac{\log(1+|\mathcal H(X)|)}{\log X}
=\Theta.
\]

Assume `Theta>1/2`. Fix a row-growth exponent `c>0` satisfying

\[
\boxed{c>1-\Theta.}
\tag{7}
\]

Choose `delta>0` so small that

\[
c+\Theta-\delta-1>0.
\tag{8}
\]

There are arbitrarily large zero-frontier spike horizons with

\[
|\mathcal H(X)|\ge X^{\Theta-\delta}.
\tag{9}
\]

For any squarefree hosts satisfying

\[
q=X^{c+o(1)},
\tag{10}
\]

one then has

\[
\frac{q|\mathcal H(X)|}{X}
\ge
X^{c+\Theta-\delta-1+o(1)}
\longrightarrow\infty.
\tag{11}
\]

Therefore every such spike obeys (5)--(6). A `Theta`-scale shell spike placed on a squarefree row of size `X^(c+o(1))` cannot be quadratically isolated once `c>1-Theta`.

At the physical horizon `H=qX`, the host row has exponent

\[
q=H^{\alpha+o(1)},
\qquad
\alpha=\frac{c}{1+c}.
\tag{12}
\]

Condition (7) is equivalent to

\[
\boxed{
\alpha>\alpha_\Theta
:=
\frac{1-\Theta}{2-\Theta}.
}
\tag{13}
\]

This threshold has the expected critical calibration:

\[
\alpha_\Theta\longrightarrow\frac13
\qquad(\Theta\downarrow1/2),
\]

while `alpha_Theta<1/3` whenever RH is false. Thus the cube-root row scale from the unconditional global pairing theorem `FD-037` reappears as the limiting zero-frontier threshold, but an actual off-critical zero pushes the spike-level protected region strictly deeper into the low-row side.

Equation (13) is a statement about **frontier-sized spikes**, not an all-horizon improvement of the global cube-root core. `FD-037` still owns the unconditional statement about every possible vanishing-occupation sequence; the present argument uses the large values supplied by `FD-046` and cannot be applied at arbitrary horizons where `mathcal H` may be much smaller.

## 3. Primorial rays are transversely blind above the threshold

Now use exactly the moving hosts from `FD-053`:

\[
q_X:=\prod_{p\le c\log X}p,
\qquad 0<c\le1.
\tag{14}
\]

The prime number theorem gives

\[
q_X=X^{c+o(1)}.
\tag{15}
\]

For large `X`, `q_X` contains the prime `2` exactly once and is therefore congruent to `2 mod 4`. Its nearest nonsquarefree witness is especially simple:

\[
\boxed{q_X^*=q_X+2.}
\tag{16}
\]

If `c>1-Theta`, equations (5)--(6) apply on every sufficiently strong zero-frontier spike sequence chosen as above. In particular the endpoint `c=1`, which `FD-053` places at

\[
q_X=H^{1/2+o(1)},
\]

always has a comparable nonsquarefree quadratic twin under false RH.

This does **not** contradict the squarefree self-cancellation of `FD-053`. Its signed ray runs through rows

\[
q_Xm,
\qquad m=1,2,\ldots,
\]

whereas the witness `q_X+2` is additive and is not on that multiplicative ray. The two facts can therefore coexist:

- the complete signed first moment along the multiplicative ray can cancel the `1/zeta(s)` source pole and balance its leading spike among squarefree multiples;
- the ambient Jordan energy at the same physical horizon already contains a nearby nonsquarefree row with essentially the same shell value.

The durable conclusion is that the one-dimensional dilation ray is **transversely blind** to the local quadratic occupation geometry. Above the threshold (13), its squarefree self-cancellation cannot be interpreted as a candidate mechanism for making the full nonsquarefree occupation numerator small.

## 4. What remains open

The result does not prove a positive constant lower bound for `U_(H,D)/E_(H,D)`. Even when the witness (5) is large, unrelated low rows can make the total denominator `E_(H,D)` much larger. Nor does it rule out escape on rows at or below

\[
q=X^{1-\Theta+o(1)},
\qquad
r=H^{\alpha_\Theta+o(1)},
\]

because there the deterministic quotient displacement `X/q` can be as large as the frontier-sized shell value itself. The endpoint is deliberately left open; the limsup exponent from `FD-046` supplies no uniform subpower margin there.

Accordingly, the live physical escape channel is narrower than the raw `FD-053` ray picture suggests. A false-RH spike can use squarefree multiplicative self-cancellation without an automatic comparable nonsquarefree additive twin only in the deeper low-row regime

\[
\alpha\le\frac{1-\Theta}{2-\Theta},
\]

or through a mechanism in which the total energy denominator overwhelms the locally transported spike. Any further improvement must therefore control the exact source inside that low-row regime rather than strengthen the already-settled moving-ray first moment above it.

## 5. Prior-art and falsification boundary

A targeted prior-art search was run around Farey discrepancy with squarefree or `k`-free denominators, Jordan-totient weighting, primorial/rough denominator restrictions, and Mertens/Farey transforms. Recent nearby literature includes Banks' work on reduced fractions with squarefree denominators, Chahal--Chaubey on pair correlation for squarefree Farey denominators, and Chahal--Chatterjee--Chaubey on `k`-free Farey denominators. Those works study restricted Farey subsequences, discrepancy/equidistribution, and local correlation; no matching result was found for the present moving Jordan-row source, additive nonsquarefree witness, or the threshold (13). No novelty is claimed for bounded-distance multiples of four, the prime number theorem, or the individual ingredients inherited from `FD-037`, `FD-046`, and `FD-053`.

No new external theorem is load-bearing. The primorial placement uses the prime number theorem already anchored in `SOURCES.md`, and the rest is an exact consequence of the line's physical coefficient law and positive Jordan norm. `SOURCES.md` therefore needs no update.

The finding is falsified if the quotient displacement bound (1), the one-Lipschitz shell law, or the conversion from `c>1-Theta` to (13) is incorrect in the stated normalization. It must not be cited as proving `U/E` has a positive pointwise limit, improving the global `FD-037` cube-root localization at every horizon, or contradicting the signed cancellations in `FD-052`--`FD-053`. Its exact contribution is the spike-level quadratic transference and the resulting zero-frontier row threshold.