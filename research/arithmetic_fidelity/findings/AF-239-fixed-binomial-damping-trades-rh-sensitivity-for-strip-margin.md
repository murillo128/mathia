# AF-239 — fixed binomial damping trades RH sensitivity for a wider zero-free band

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `RH-TARGET-METRIC`, `CANCELLATION-COHERENCE`, `FILTER-TRADEOFF`, `NO-NOVELTY-CLAIM`

## Claim

AF-238 shows that ordinary initial truncation of the completed local `xi'/xi` jet is not cancellation-coherent: even a zero already known to lie on the critical line can create a spurious exponential root rate when its binomial orbit is interrupted. A natural repair is therefore to keep the **entire** binomial orbit but damp high local orders smoothly.

Let

\[
Q(w):=\frac{\xi'}{\xi}(1+w)=\sum_{j\ge0} b_j w^j
\tag{1}
\]

and, for a fixed real parameter `0<t<=1`, define the fully supported damped Li transform

\[
\Lambda_n(t)
:=\sum_{k=1}^n \binom nk t^k b_{k-1}.
\tag{2}
\]

Then its ordinary generating function is exactly

\[
\boxed{
G_t(z):=\sum_{n\ge1}\Lambda_n(t)z^{n-1}
=\frac{t}{(1-z)^2}
Q\!\left(\frac{tz}{1-z}\right).
}
\tag{3}
\]

A nontrivial zero `rho=beta+i gamma` of `zeta` produces a pole of `G_t` at

\[
z_\rho(t)
=\frac{\rho-1}{\rho-1+t}.
\tag{4}
\]

Consequently

\[
|z_\rho(t)|<1
\iff
\beta>1-\frac t2.
\tag{5}
\]

Since the nontrivial zero set is invariant under `rho -> 1-rho`, Cauchy--Hadamard gives the exact root-rate criterion

\[
\boxed{
\limsup_{n\to\infty}|\Lambda_n(t)|^{1/n}\le1
\iff
\zeta(s)\text{ has no zero with }\Re s>1-\frac t2
}
\tag{6}
\]

or, equivalently,

\[
\boxed{
\limsup_{n\to\infty}|\Lambda_n(t)|^{1/n}\le1
\iff
\frac t2\le \Re\rho\le1-\frac t2
\quad\text{for every nontrivial zero }\rho.
}
\tag{7}
\]

At `t=1`, `(2)` is the usual Li sequence and `(6)` reduces to the AF-235 RH criterion. For every fixed `0<t<1`, however, the decoded property is only a **wider symmetric zero-free band**. Zeros in

\[
\frac12<\beta\le1-\frac t2
\tag{8}
\]

are invisible to the binary root-rate test.

Thus fixed damping does repair the specific cancellation pathology exposed by AF-238 for each critical-line pole, but it pays for that repair by moving the discrimination boundary away from the critical line. In Arithmetic Fidelity terms:

\[
\boxed{
\text{fixed cancellation margin}
\quad\Longleftrightarrow\quad
\text{loss of near-critical off-line sensitivity}.
}
\tag{9}
\]

This rules out the simplest full-orbit regularization as an RH-sufficient replacement for the undamped Li transform.

## Derivation

### The damped local jet has a closed generating function

Starting from `(2)` and using

\[
\sum_{n\ge k}\binom nk z^{n-1}
=\frac{z^{k-1}}{(1-z)^{k+1}},
\tag{10}
\]

we obtain, for `|z|` small,

\[
\begin{aligned}
G_t(z)
&=\sum_{k\ge1}t^k b_{k-1}
  \frac{z^{k-1}}{(1-z)^{k+1}}\\
&=\frac{t}{(1-z)^2}
  \sum_{j\ge0}b_j
  \left(\frac{tz}{1-z}\right)^j,
\end{aligned}
\tag{11}
\]

which is `(3)`.

The Möbius argument of `Q` is

\[
w=\frac{tz}{1-z},
\qquad
s=1+w=1+\frac{tz}{1-z}.
\tag{12}
\]

Because `xi'/xi` is meromorphic with poles exactly at the nontrivial zeros of `zeta`, solving `s=rho` gives `(4)`. The map is injective for fixed `t>0`, so a zero of multiplicity `m` gives a genuine pole of the same multiplicity at its image; there is no cancellation between distinct zero locations.

### The unit-circle boundary moves linearly with the damping

For `rho=beta+i gamma`,

\[
|\rho-1+t|^2-|\rho-1|^2
=2t(\beta-1)+t^2.
\tag{13}
\]

Hence

\[
|z_\rho(t)|<1
\iff
|\rho-1|<|\rho-1+t|
\iff
\beta>1-\frac t2,
\tag{14}
\]

proving `(5)`.

If such a zero exists, `G_t` has a pole strictly inside the unit disk, so its Taylor radius is strictly smaller than `1` and

\[
\limsup |\Lambda_n(t)|^{1/n}>1.
\tag{15}
\]

Conversely, if no zero satisfies `(5)`, then `G_t` has no zero-induced singularity in `|z|<1`. The only other obstruction visible in `(3)` is at the boundary point `z=1`, where the Möbius coordinate tends to infinity; there is no additional interior singularity. Therefore the Taylor radius is at least `1`, giving

\[
\limsup |\Lambda_n(t)|^{1/n}\le1.
\tag{16}
\]

This proves `(6)`. Reflection symmetry of the zero set turns the one-sided condition into `(7)`.

### Full damping is cancellation-coherent for an individual critical-line zero

Using the paired Hadamard zero expansion, the contribution of one reflected zero may be written in the familiar Li-type form

\[
1-\left(1-\frac t\rho\right)^n.
\tag{17}
\]

Equivalently, in the `s=1` local coordinate used by `(1)`, a pole at `a=rho-1` contributes

\[
1-\left(1+\frac t a\right)^n.
\tag{18}
\]

If `Re(rho)=1/2`, then

\[
\left|1+\frac t{\rho-1}\right|^2
=1-\frac{t(1-t)}{|\rho-1|^2}.
\tag{19}
\]

Thus for every fixed `0<t<1` and every individual critical-line zero,

\[
\left|1+\frac t{\rho-1}\right|<1.
\tag{20}
\]

The full damped orbit therefore suppresses rather than amplifies the known critical-line pole that generated AF-238's truncated-jet artifact. This is genuine cancellation coherence: the filter changes the whole binomial orbit, rather than cutting it before cancellation completes.

But the margin is not uniform over the zero set. As `|gamma|->infinity`, the right-hand side of `(19)` tends to `1`. Fixed damping therefore gives each critical-line zero a strict inward response factor while providing no height-independent spectral gap.

### The same deformation loses a strip of off-line sensitivity

For a zero on the right of the critical line, the local response becomes exponentially expanding only when

\[
\beta>1-\frac t2.
\tag{21}
\]

Hence decreasing `t` moves the detection threshold to the right. The regularization parameter and the missed strip width are not independent:

\[
\left(1-\frac t2\right)-\frac12
=\frac{1-t}{2}.
\tag{22}
\]

A fixed amount of damping `1-t` therefore creates exactly half that amount of unresolved real-part width on each side of the critical line.

At `t=1` this blind strip collapses and full RH sensitivity returns, but `(19)` simultaneously loses its strict contraction: every critical-line zero has modulus-one response, which is exactly the undamped Li geometry.

## Prior art and novelty assessment

The underlying use of Li-type coefficients to characterize zero-free half-planes is classical. Pedro Freitas, **“A Li-Type Criterion for Zero-Free Half-Planes of Riemann's Zeta Function,”** *Journal of the London Mathematical Society* 73(2) (2006), 399--414, DOI `10.1112/S0024610706022599`, arXiv:`math/0507368`, proves that a parameterized Li family characterizes the absence of zeros from half-planes `Re(s)>tau/2`. Freitas also explicitly notes that away from the ordinary `tau=1` Li point, the positive- and negative-index forms that coincide at `tau=1` must be distinguished.

Bombieri and Lagarias, **“Complements to Li's Criterion for the Riemann Hypothesis,”** *Journal of Number Theory* 77(2) (1999), 274--287, DOI `10.1006/jnth.1999.2392`, provide the general multiset/conformal-mapping framework behind Li-type radius and positivity criteria. Keiper's 1992 generating-function formulation is the classical source already used in AF-235 for the unit-disk/root-rate viewpoint.

No novelty is claimed for parameterized Li criteria, Möbius mapping of zero half-planes to disks, or Cauchy--Hadamard detection of an interior pole. The family `(2)` is introduced here only as the most direct **full-orbit damping of the exact local-jet representation left open by AF-238**. The durable Arithmetic Fidelity result is the exact tradeoff `(5)--(9)`: this cancellation-coherent regularization moves the exponential discrimination boundary from `Re(s)=1/2` to `Re(s)=1-t/2` and therefore cannot, at fixed `t<1`, retain the AF-235 binary RH endpoint.

The decoded zero-free region is squarely within classical Li-type prior art; the finding is an obstruction/placement result for the current Mathia filter question, not a new zero-free criterion.

## Exact controls and boundaries

**Undamped control.** At `t=1`, `(3)` is the standard Li generating function, `Lambda_n(1)=lambda_n`, and `(6)` is exactly RH.

**Critical-line control.** Equation `(19)` proves that any `0<t<1` removes AF-238's per-pole exponential artifact for a critical-line zero when the full orbit is retained. This distinguishes full damping from prefix truncation.

**Near-critical off-line control.** A hypothetical zero with `1/2<beta<=1-t/2` remains outside or on the unit disk in the damped coordinate and cannot force root rate greater than one. The filter therefore cannot distinguish it from the RH-compatible side using the AF-235 decoder.

**High-zero control.** The contraction in `(19)` tends to zero in logarithmic strength like `t(1-t)/(2 gamma^2)`. There is no uniform damping gap over all critical-line zeros.

**No source compression.** Equation `(2)` still uses all local coefficients through order `n`. It solves neither the source-depth bill from AF-236 nor the goal of producing a cheaper prime-side representation. It is only a clean test of whether smooth full-orbit regularization can repair cancellation while preserving the same endpoint.

**No theorem that the wider band holds.** For `t<1`, `(6)` is a criterion for a weaker zero-free statement, not an unconditional assertion that zeta satisfies it. In particular, classical zero-free regions approaching `Re(s)=1` do not by themselves give a fixed global band `Re(s)<=1-t/2` for arbitrary fixed `t` close to one.

## Consequences for the research frontier

AF-238's filter-separation problem now has a sharper boundary. The two most obvious static choices fail in complementary ways:

1. initial local-jet truncation breaks complete binomial cancellation and can manufacture root rate greater than one from an RH-compatible zero;
2. full fixed damping restores per-zero cancellation coherence but shifts the detection boundary away from the critical line by exactly `(1-t)/2`.

A viable deformation therefore cannot choose a fixed regularization strength. The next natural question is whether a **scale-dependent family `t_n -> 1`**, or a genuinely nonlocal contour/orbit-completion filter, can retain enough finite-`n` cancellation to suppress AF-238-type artifacts while asymptotically returning the unit-circle boundary to `Re(s)=1/2`.

That question needs a uniform theorem, not pointwise pole algebra: the filter must control the aggregate high-zero contribution and prevent a varying parameter from tuning away the very off-critical exponential signal it is meant to retain. Any proposed `t_n` schedule should therefore be audited simultaneously for (i) critical-line aggregate root rate, (ii) stability of an off-critical dominant-pole limsup, and (iii) actual source-access cost. Fixed-`t` damping is now ruled out as the endpoint-preserving solution.