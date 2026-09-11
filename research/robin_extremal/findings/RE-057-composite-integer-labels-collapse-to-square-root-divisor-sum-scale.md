# RE-057 — composite integer labels collapse to square-root divisor-sum scale

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + DIVISOR-SUM-REALIZATION-GATE + PRIMALITY-CERTIFICATE + SHARP-SQUARE-ROOT-COMPOSITE-PENALTY + GENERALIZED-CONTROL-BOUNDARY + PRIOR-ART-CLASSIFIED`.

`RE-055` and `RE-056` show that PNT-scale density, one common label source for every formal CA layer, synchronized all-layer event-free chambers, a subpower gap ceiling, and even **integer-valued labels** can all be reproduced by matched controls. The missing distinction can now be made exact at the first multiplicative transition. The prime-form increment used throughout those controls,

\[
\lambda_1(q)=\log(1+q^{-1}),
\tag{1}
\]

is not merely a convenient smooth model when `q` is required to act as a new ordinary integer factor. It is a **primality certificate**. If an integer state `N` is coprime to `q>1`, then the actual normalized divisor-sum gain from adjoining `q` is

\[
\Delta_\sigma(N;q)
:=
\log\frac{\sigma(Nq)/(Nq)}{\sigma(N)/N}
=
\log\frac{\sigma(q)}q.
\tag{2}
\]

Hence

\[
\boxed{
\Delta_\sigma(N;q)=\lambda_1(q)
\quad\Longleftrightarrow\quad
\sigma(q)=q+1
\quad\Longleftrightarrow\quad
q\text{ is prime}.
}
\tag{3}
\]

For a composite integer label the failure is not a small rounding defect. Every composite `q` satisfies

\[
\boxed{
\sigma(q)\ge q+\sqrt q+1,
}
\tag{4}
\]

with equality exactly for squares of primes. Consequently

\[
\boxed{
\Delta_\sigma(N;q)-\lambda_1(q)
\ge
\log\!\left(
\frac{1+q^{-1/2}+q^{-1}}{1+q^{-1}}
\right)
=
q^{-1/2}+O(q^{-1}).
}
\tag{5}
\]

The formal first-layer mass is only

\[
\lambda_1(q)=q^{-1}+O(q^{-2}),
\tag{6}
\]

so a composite label incurs an unavoidable ordinary-divisor contribution larger by a factor of order `sqrt(q)`.

This discrepancy has a direct event-scale interpretation. Put

\[
g(x)=\frac1{x\log x}
\tag{7}
\]

as in `RE-040`, and for a new coprime integer factor `q` define the actual one-step tangent coordinate `\zeta_\sigma(q)` by

\[
g(\zeta_\sigma(q))
=
\frac{\log(\sigma(q)/q)}{\log q}.
\tag{8}
\]

For composite `q->infinity`, (4) gives

\[
\boxed{
\zeta_\sigma(q)
\le
(2+o(1))\sqrt q.
}
\tag{9}
\]

By contrast, the generalized first-layer event coordinate used in `RE-055`--`RE-056` is determined by

\[
g(\eta_1(q))
=
\frac{\log(1+q^{-1})}{\log q}
\tag{10}
\]

and satisfies

\[
\eta_1(q)=q+\frac12+O((\log q)^{-1}).
\tag{11}
\]

Therefore

\[
\boxed{
\frac{\zeta_\sigma(q)}{\eta_1(q)}
\le
\frac{2+o(1)}{\sqrt q}
\longrightarrow0
\qquad(q\text{ composite}).
}
\tag{12}
\]

The constant `2` in (9) is asymptotically sharp: for `q=p^2` with `p` prime,

\[
\frac{\sigma(q)}q
=1+p^{-1}+p^{-2},
\tag{13}
\]

so

\[
\frac{\log(\sigma(q)/q)}{\log q}
=
\frac{1+o(1)}{2p\log p}
=
g((2+o(1))p),
\tag{14}
\]

and hence

\[
\boxed{
\zeta_\sigma(p^2)=(2+o(1))p=(2+o(1))\sqrt q.
}
\tag{15}
\]

Thus the integer-label controls of `RE-056` cannot be upgraded to ordinary divisor-sum realizations by adding only coprimality, pairwise-coprimality, or an abstract unique-factorization convention. A composite formal label near scale `q` does **not** behave as an ordinary first-layer atom near scale `q`; its internal divisors inject at least square-root-scale mass and move the corresponding tangent coordinate down to `O(sqrt(q))`. Requiring the exact ordinary `sigma` response at the first-layer transition collapses the generalized label class immediately to actual primes.

This is a boundary result, not a solution of Robin's inequality. It does not prove a new gap theorem for the primes, exclude the false-RH adaptive fans of `RE-040`, or show that every quotient of consecutive CA states is prime. It identifies the first exact piece of multiplicative arithmetic that the current matched controls cannot fake: **prime atoms have no internal proper divisor**, and the normalized divisor-sum functional detects that absence at a quantitatively sharp scale.

## 1. The ordinary normalized divisor-sum transition factors through `sigma(q)`

Let

\[
F(n):=\log\frac{\sigma(n)}n.
\tag{16}
\]

If `gcd(N,q)=1`, multiplicativity of `sigma` gives

\[
\frac{\sigma(Nq)}{Nq}
=
\frac{\sigma(N)}N\frac{\sigma(q)}q,
\tag{17}
\]

and therefore (2). The generalized first-layer law of `RE-053`--`RE-056` instead assigns to the same label the increment (1). Equality between the two is equivalent to

\[
\sigma(q)=q+1.
\tag{18}
\]

For every integer `q>1`, the divisors `1` and `q` are always present. Equality in (18) says that there is no other positive divisor, which is exactly primality. This proves (3) without any asymptotic input.

The coprimality condition is not an artificial strengthening. A genuine first-layer CA transition introduces a previously absent prime coordinate. If `q` shares a prime factor with `N`, multiplication by `q` changes one or more already active prime exponents and is not the one-new-atom transition modeled by (1).

## 2. Composite labels have an unavoidable square-root divisor contribution

Let `q` be composite. Choose a proper divisor `d` with

\[
2\le d\le\sqrt q.
\tag{19}
\]

If `d<sqrt(q)`, then `q/d` is a distinct proper divisor and

\[
d+\frac qd\ge2\sqrt q.
\tag{20}
\]

If `d=sqrt(q)`, that divisor alone contributes `sqrt(q)`. In either case, together with `1` and `q`,

\[
\sigma(q)\ge q+\sqrt q+1.
\tag{21}
\]

Equality can occur only in the square case with no additional divisors; then `sqrt(q)` must be prime. Conversely, if `q=p^2` with `p` prime, its divisors are exactly `1,p,p^2`, so equality holds. This proves (4) and its equality classification.

Dividing by `q` and taking logarithms gives

\[
\Delta_\sigma(N;q)
\ge
\log(1+q^{-1/2}+q^{-1}).
\tag{22}
\]

Subtracting (1) yields the first expression in (5). Since

\[
\frac{1+q^{-1/2}+q^{-1}}{1+q^{-1}}
=
1+\frac{q^{-1/2}}{1+q^{-1}},
\tag{23}
\]

the logarithm is `q^(-1/2)+O(q^(-1))`. The prime-form increment (6) is one full square-root scale smaller.

This lower bound is the correct worst-case order. Prime squares attain (21) exactly, so no uniform composite penalty larger than order `q^(-1/2)` is possible.

## 3. The multiplicative error becomes a sharp event-coordinate collapse

Divide (22) by `log q`. Uniformly over composite `q`,

\[
\frac{\log(\sigma(q)/q)}{\log q}
\ge
\frac{1+o(1)}{\sqrt q\log q}.
\tag{24}
\]

The function `g(x)=1/(x log x)` is strictly decreasing for large `x`. For every fixed `delta>0`,

\[
g((2+\delta)\sqrt q)
=
\left(\frac{2}{2+\delta}+o(1)\right)
\frac1{\sqrt q\log q}
<
\frac{1+o(1)}{\sqrt q\log q}.
\tag{25}
\]

Equations (8), (24), and monotonicity of `g` imply

\[
\zeta_\sigma(q)<(2+\delta)\sqrt q
\tag{26}
\]

for all sufficiently large composite `q`. Since `delta` is arbitrary, (9) follows.

For a prime square `q=p^2`, equation (13) gives

\[
\log(1+p^{-1}+p^{-2})
=p^{-1}+O(p^{-2}),
\tag{27}
\]

while `log q=2 log p`. Hence the left side of (8) is

\[
\frac{1+o(1)}{2p\log p}.
\tag{28}
\]

But

\[
g(2p)
=
\frac1{2p\log(2p)}
=
\frac{1+o(1)}{2p\log p},
\tag{29}
\]

which proves the sharpness statement (15) by monotone inversion.

In the synthetic prime-form law, on the other hand,

\[
\frac{\lambda_1(q)}{\log q}
=
\frac{1+o(1)}{q\log q}.
\tag{30}
\]

The exact expansion (11) was already used in `RE-055`--`RE-056`; even the weaker `eta_1(q)/q->1` is enough to combine with (9) and prove (12).

## 4. What this removes from the matched-control frontier

`RE-056` deliberately proved only that the **integer lattice** does not restore ordinary-prime rigidity. Its set `Q` may contain composites and multiplicative dependencies, while every formal label is nevertheless assigned the prime-like first-layer gain `log(1+1/q)` and the corresponding all-layer CA-form increments.

The present calculation shows exactly where such a control stops being an ordinary divisor-sum model. If a composite label `q` is adjoined as a new coprime integer factor, ordinary multiplicativity exposes all divisors of `q`; the local gain is (2), not (1), and differs by at least the square-root amount (5). Pairwise coprimality between different labels does not help, because the discrepancy is internal to `q` itself. Declaring the labels to be free formal generators also does not help if the target functional is required to be the ordinary integer `sigma` function rather than a generalized Euler product.

There is therefore no gradual interpolation

\[
\text{real generalized labels}
\to
\text{integer generalized labels}
\to
\text{coprime composite labels}
\to
\text{ordinary CA first-layer atoms}
\tag{31}
\]

that preserves the same local transition law. The last step is a hard gate: exact first-layer divisor-sum realization forces primality label by label.

This also does not conflict with the classical possibility of a composite quotient between consecutive CA numbers. A quotient such as a product of two primes represents simultaneous genuine prime-coordinate transitions. Its ordinary divisor-sum gain factorizes into the gains of those prime atoms; it is **not** one composite first-layer atom carrying the synthetic mass `log(1+1/q)`.

## 5. Prior-art and novelty boundary

The ingredients behind (3)--(5) are classical and elementary. The multiplicativity of `sigma`, the formula for `sigma(p^a)`, and the characterization `sigma(q)=q+1` iff `q` is prime are standard. The stronger composite bound `sigma(q)>=q+sqrt(q)+1`, with equality at prime squares, is also classical and follows directly from divisor pairing; the proof is included above, so no external theorem is load-bearing. The established CA literature already organizes genuine states by prime-power coordinates.

The line-specific contribution here is not a new characterization of primes. It is the quantitative splice with the `RE-055`--`RE-056` matched controls: the classical composite excess is transported through the exact CA tangent map `g`, where it becomes the sharp collapse

\[
q\quad\longmapsto\quad O(\sqrt q)
\tag{32}
\]

for the event coordinate of any composite label interpreted as one new ordinary factor. A targeted literature audit found the classical divisor-sum inequalities and standard CA prime-factor structure, but no prior statement using this event-coordinate comparison to delimit generalized integer controls. No new external source is needed for the proof, so `SOURCES.md` is unchanged.

## 6. Boundary conditions and consequences

The result applies to a **new coprime factor transition**, which is the ordinary-integer analogue of the formal first-layer atom in `RE-056`. It does not claim (9) for multiplying an arbitrary state by a composite `q` sharing active prime factors; such a move changes several existing exponent coordinates and must be decomposed in the genuine prime-power lattice before comparing CA events.

Nor does the theorem itself supply a usable distribution estimate for the surviving prime labels. Once exact ordinary divisor-sum realization is imposed, the matched-control class simply collapses back to the ordinary prime source, so the hard RH-facing problem remains: extract a consequence of primality/multiplicative source identity that conflicts with the false-RH adaptive fan. What has changed is the location of that missing information. It is no longer reasonable to search for the next obstruction by merely strengthening `RE-056` with generic integer or coprimality conditions while retaining prime-form label increments.

A productive continuation must use a relation that follows from the **actual prime factorization** and interacts with the fan without merely assuming a stronger prime-gap theorem. Natural candidates already present in the line are the exact accumulated CA mass `Y=Phi(Z)` and the standard/reciprocal prime-race coupling of `RE-040`; any future matched control for those mechanisms must preserve ordinary `sigma` at the prime-coordinate level rather than treating composite integers as substitute atoms.