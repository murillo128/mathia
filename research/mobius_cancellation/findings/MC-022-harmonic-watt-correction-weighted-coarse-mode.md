# MC-022 — The harmonic/Watt correction contains a doubled-scale weighted coarse mode

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `DECISIVE-NEGATIVE`, `NO-NOVELTY-CLAIM`.

## Claim

The pointwise correction between the centered harmonic endpoint kernel of `MC-021` and Nigel Watt's classical sawtooth kernel is **not** an independently cheap boundary perturbation at the RH scale. Exact subtraction of the two Huxley–Watt identities shows that its Möbius quadratic form contains a doubled-scale weighted Mertens quantity whose critical bound is itself equivalent to RH, up to explicit lower-scale terms.

Write

\[
M(x)=\sum_{n\le x}\mu(n),
\qquad
H(x)=\sum_{n\le x}\frac{\mu(n)}n,
\qquad
J(x)=\sum_{n\le x}\frac{\mu(n)\log n}{n}.
\tag{1}
\]

For `y>=1`, let

\[
W(y)=\frac12-\{y\},
\qquad
\kappa(y)=y\bigl(H_{\lfloor y\rfloor}^{(1)}-\log y-\gamma\bigr),
\qquad
\delta(y)=\kappa(y)-W(y).
\tag{2}
\]

Define the three quadratic forms

\[
Q_W(N)=\sum_{m,n\le N}\mu(m)\mu(n)
W\!\left(\frac{N^2}{mn}\right),
\tag{3}
\]

\[
B_\kappa(N)=\sum_{m,n\le N}\mu(m)\mu(n)
\kappa\!\left(\frac{N^2}{mn}\right),
\tag{4}
\]

and

\[
C_\delta(N)=B_\kappa(N)-Q_W(N)
=\sum_{m,n\le N}\mu(m)\mu(n)
\delta\!\left(\frac{N^2}{mn}\right).
\tag{5}
\]

Finally set

\[
D(x)=M(x)-xH(x).
\tag{6}
\]

Then the exact `g=1` identity from `MC-020` and the exact `g(n)=1/n` identity from `MC-021` give

\[
\boxed{
\begin{aligned}
C_\delta(N)
={}&D(N^2)
+N^2\Bigl[
2H(N)(1+J(N))\\
&\hspace{22mm}-(2\log N+\gamma-1)H(N)^2
\Bigr]\\
&-2M(N)-\frac12M(N)^2.
\end{aligned}
}
\tag{7}
\]

The new coarse term is not benign. One has the exact Mellin identity

\[
\boxed{
\int_1^\infty D(x)x^{-s-1}\,dx
=-\frac{1}{s(s-1)\zeta(s)}
}
\qquad (\Re s>1),
\tag{8}
\]

and consequently

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
D(x)=O_\varepsilon(x^{1/2+\varepsilon})
\text{ for every }\varepsilon>0.
}
\tag{9}
\]

Thus the visual/asymptotic fact from `VIS-003` that `delta(y)=O(1/y)` in the large-`y` bulk does not imply that the associated Möbius quadratic form is a lower-order information carrier. At square scale, exact summation reconstructs an RH-equivalent weighted coarse mode at `N^2`.

More precisely, in any scale-doubling bootstrap where the lower-scale critical estimates

\[
M(N)=O_\varepsilon(N^{1/2+\varepsilon}),
\quad
H(N)=O_\varepsilon(N^{-1/2+\varepsilon}),
\quad
1+J(N)=O_\varepsilon(N^{-1/2+\varepsilon})
\tag{10}
\]

are already available as induction hypotheses, equation (7) gives

\[
C_\delta(N)=D(N^2)+O_\varepsilon(N^{1+\varepsilon})
\tag{11}
\]

after the usual epsilon relabelling. Therefore proving a separate critical-scale estimate

\[
C_\delta(N)=O_\varepsilon(N^{1+\varepsilon})
\tag{12}
\]

is, at that transfer step, exactly as strong as producing the next-scale critical estimate for `D(N^2)`. The harmonic endpoint can still be useful through **coupled cancellation** between the Watt part, the correction, and the centered lower-scale coefficients, but the correction cannot be treated as an automatically cheaper remainder merely because it is pointwise small away from the corner.

## 1. Exact subtraction of the two square-scale identities

`MC-020` records the Huxley–Watt specialization `g=1` in the form

\[
M(N^2)
=2M(N)-N^2H(N)^2+\frac12M(N)^2-Q_W(N).
\tag{13}
\]

Hence

\[
Q_W(N)
=2M(N)-N^2H(N)^2+\frac12M(N)^2-M(N^2).
\tag{14}
\]

`MC-021` records the `g(n)=1/n` endpoint as

\[
H(N^2)
=2H(N)(1+J(N))
-(2\log N+\gamma)H(N)^2
-\frac{B_\kappa(N)}{N^2},
\tag{15}
\]

so

\[
B_\kappa(N)
=N^2\Bigl[
2H(N)(1+J(N))
-(2\log N+\gamma)H(N)^2
-H(N^2)
\Bigr].
\tag{16}
\]

Subtracting (14) from (16), using `C_delta=B_kappa-Q_W`, and grouping

\[
M(N^2)-N^2H(N^2)=D(N^2)
\]

gives (7) exactly. No asymptotic expansion of `kappa`, no continuum spectral approximation, and no zero formula enters this step.

This is the decisive finite decomposition requested by the proposed harmonic-endpoint/Watt-boundary clue. It identifies what the pointwise kernel correction becomes after being tested against the exact Möbius signs.

## 2. The weighted coarse mode has the critical zero boundary

The quantity `D` also has the elementary partial-summation form

\[
H(x)=\frac{M(x)}x+\int_1^x\frac{M(t)}{t^2}\,dt,
\]

hence

\[
D(x)=-x\int_1^x\frac{M(t)}{t^2}\,dt.
\tag{17}
\]

For the Mellin transform, absolute convergence when `Re(s)>1` permits reversing the sum and integral:

\[
\begin{aligned}
\int_1^\infty D(x)x^{-s-1}\,dx
&=\sum_{n\ge1}\mu(n)
\int_n^\infty\left(1-\frac{x}{n}\right)x^{-s-1}\,dx\\
&=-\frac1{s(s-1)}\sum_{n\ge1}\frac{\mu(n)}{n^s},
\end{aligned}
\tag{18}
\]

which proves (8).

Assume RH. The classical Mertens criterion gives

\[
M(x)=O_\varepsilon(x^{1/2+\varepsilon}),
\]

and `MC-020` records the corresponding bound

\[
H(x)=O_\varepsilon(x^{-1/2+\varepsilon}).
\]

Equation (6) therefore gives the forward implication in (9).

Conversely, assume the bound for `D` in (9). On every compact subset of `Re(s)>1/2`, choose `epsilon` smaller than the distance to the critical line. The integral in (8) then converges locally uniformly and defines a holomorphic function `F(s)` throughout `Re(s)>1/2`. On `Re(s)>1`,

\[
s(s-1)\zeta(s)F(s)=-1.
\tag{19}
\]

Let `Z_0(s)=(s-1)zeta(s)`, which is holomorphic across `s=1`. By the identity theorem,

\[
sZ_0(s)F(s)=-1
\tag{20}
\]

throughout the connected half-plane `Re(s)>1/2`. A nontrivial zero `rho` of zeta in that half-plane would make the left side vanish, contradicting (20). The functional equation then gives RH. This proves (9) without importing the desired zero-free region into the definition of `D`.

The mechanism is closely analogous to the first Riesz coarse-mode audit in `MC-019`, but the carrier is different: `D(x)` is the centered reciprocal-weighted Mertens combination produced by subtracting the two Huxley–Watt endpoints.

## 3. Why pointwise kernel smallness does not buy a polynomial factor

`VIS-003` proves, for `y -> infinity`,

\[
\kappa(y)
=W(y)-\frac{B_2(\{y\})}{2y}+O(y^{-2}),
\]

uniformly in the fractional part. Thus `delta(y)=O(1/y)` in the product-coordinate bulk. It is tempting to regard `C_delta` as a perturbative Bernoulli/boundary correction to Watt's quadratic form.

Equation (7) blocks that inference. The kernel is sampled on the dense multiplicative grid `y=N^2/(mn)`, and the summation against `mu(m)mu(n)` reorganizes the correction into a next-scale weighted global quantity plus lower-scale terms. An entrywise or bulk-versus-corner estimate that ignores this exact arithmetic recombination can therefore misclassify the information content of the correction.

This does not say that `C_delta` is numerically large, nor that every decomposition of it is useless. It says that a proof of (12) cannot be credited as a cheap perturbative estimate in a critical scale-doubling argument unless its proof uses genuinely weaker information than the next-scale bound for `D`. Equation (7) is the audit identity for that claim.

## 4. Prior art and novelty boundary

The parent square-scale identities are prior art: M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function*, Chebyshevskii Sbornik 19(3) (2018), 20–34, DOI `10.22405/2226-8383-2018-19-3-20-34`, arXiv `1807.05890`. Their theorem explicitly allows arbitrary totally multiplicative `g`, including both endpoints used above.

Nigel Watt studies the sawtooth kernel

\[
W(1/(xy))=\frac12+\left\lfloor\frac1{xy}\right\rfloor-\frac1{xy}
\]

and its spectrum in *On eigenvalues of the kernel ...*, Journal de Théorie des Nombres de Bordeaux 31 (2019), 653–662, DOI `10.5802/jtnb.1099`, with related arXiv work `1812.01039`. The harmonic-number/Euler–Maclaurin comparison producing `delta(y)` is classical and is already audited in `VIS-003`.

Weighted Möbius sums and Mellin transforms of Mertens-type quantities are classical analytic-number-theory objects; `MC-019` already records adjacent Riesz-mean literature. A targeted search for the exact combination `M(x)-x sum_{n<=x} mu(n)/n`, the `g=1` versus `g=1/n` Huxley–Watt subtraction, and the harmonic/Watt correction did not locate an authoritative source presenting equation (7) as this square-scale information audit. That negative search is not evidence of novelty, so no novelty claim is made for (7), (8), or (9).

The durable contribution here is narrower: **within the active `MC-021` mechanism, the exact difference between the apparently new harmonic kernel and Watt's classical bulk kernel contains a next-scale RH-equivalent weighted coarse mode.** This materially changes how the candidate must be attacked.

## 5. Boundaries and decisive continuation

This finding does not kill the full `g(n)=1/n` endpoint. It kills the specific route in which the harmonic kernel is treated as Watt's known carrier plus an independently inexpensive correction and the two pieces are bounded separately.

A surviving positive mechanism must preserve at least one cancellation that such a split destroys. Concretely, it may:

- prove a signed relation between `Q_W(N)` and `C_delta(N)` that cancels the weighted coarse mode before either term is separately estimated;
- use the exact coupled recursion (15) together with an independently weaker arithmetic estimate that simultaneously controls `H`, `1+J`, and the full `B_kappa` without isolating `D(N^2)` as an input;
- expose a structural decomposition of `C_delta` whose difficult component is cancelled by another term in (7), with all remaining pieces controlled below the RH-equivalent boundary.

A proposed continuation fails if, after exact recombination, it requires the bound (9) for `D` at the next scale, or an analytically equivalent zero-free statement, as an independent hypothesis. The next useful question is therefore about **coupled cancellation across the decomposition**, not about proving that the Bernoulli/boundary correction is small in isolation.

## Consequence for the harmonic-endpoint clue

The clue asking whether `MC-021` can be split into Watt's sawtooth form plus a cheaper Bernoulli/boundary correction is resolved in narrowed form. The exact split exists, but its correction carries the next-scale quantity `D(N^2)` modulo explicit lower-scale terms, and `D` has the RH-equivalent critical boundary (9). The correction is therefore not a free polynomial gain.

The clue's remaining fertile residue is the coupled route: determine whether the **unsplit** harmonic endpoint, or a signed interaction between its Watt and correction pieces, forces cancellation that disappears under separate budgets.