# MC-477 — Low-denominator envelope admits denominator-free character completion

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-476` leaves one concrete restriction-style escape for the empty-vector rough×rough term: do not apply the coefficient-uniform restriction theorem at zero frequency, but use the low-denominator Fourier representation of the Bera--Viswanadham/Ramaré--Ruzsa enveloping sieve and couple each rational frequency to the translated-ratio character phase before positive closure.

That first coupling can be priced exactly in the prime-conductor source frame.

Let `p` be prime, let `chi` be a nonprincipal multiplicative character modulo `p`, let

\[
K_h(n)=\chi(n+h)\overline{\chi(n)},
\]

and assume `h not congruent to 0 (mod p)`. Let `I` be any integer interval of length `H<=p`. For every integer `q>=1` with `(q,p)=1` and every reduced residue `a (mod q)`, define

\[
S_{q,a}(I):=\sum_{n\in I}K_h(n)e(an/q).
\tag{1}
\]

Then uniformly in `q`, `a`, `I`, and `h`,

\[
\boxed{
|S_{q,a}(I)|\ll \sqrt p\log(2p).
}
\tag{2}
\]

The notable feature is **the absence of any power of the rational denominator `q`**. Completing modulo `pq` does not create `pq` genuinely active Fourier modes: Chinese-remainder orthogonality leaves exactly `p` modes, and the `q` factor from the complete `q`-sum cancels the `1/(pq)` Fourier normalization.

Now use the Bera--Viswanadham enveloping-sieve Fourier expansion in the pair-sieve specialization from `MC-476`. With `z_0=2`, its nonzero rational frequencies have squarefree denominator

\[
q\le z^2,\qquad q\mid P(2,z),
\]

and Lemma 3.2 gives

\[
|w(a/q)|\ll \frac{1}{G(z)\sqrt q}.
\tag{3}
\]

Because the source conductor prime `p` is removed from the sieve product in the `MC-476` setup, every such denominator is coprime to `p`. Therefore `(2)` applies termwise. The total coefficient mass has the elementary upper bound

\[
\sum_{q\le z^2}\sum_{a\bmod q}^{*}|w(a/q)|
\ll \frac1{G(z)}\sum_{q\le z^2}\frac{\varphi(q)}{\sqrt q}
\ll \frac{z^3}{G(z)}.
\tag{4}
\]

Consequently, wherever the enveloping weight `beta` is represented by that expansion,

\[
\boxed{
\left|\sum_{n\in I}K_h(n)\beta(n)\right|
\ll
\frac{z^3}{G(z)}\sqrt p\log(2p).
}
\tag{5}
\]

This is a genuine reduction in representation complexity relative to the exact pair-sieve mask: the exponential/full-primorial costs of `MC-473`--`MC-475` are replaced, under crude coefficientwise summation, by the polynomial cutoff cost `z^3/G(z)`. It is **not** yet a bound for the exact rough×rough sum. The missing step is still the signed replacement between the exact pair-sieve indicator and the enveloping object; pointwise majorization alone is invalid inside the complex character sum.

The estimate also locates the quantitative window of this simplest coupling. If the target scale is the natural sifted mass `H/G(z)`, the coefficientwise bound can only yield a strict conductor-power gain when, up to logarithms,

\[
z^3\sqrt p\ll H.
\tag{6}
\]

Thus the generic admissible restriction range `z<=H^{1/4}` does not by itself guarantee a useful conductor saving. The low-denominator representation removes the primorial dimension, but a further structural gain in the `(q,a)` family or a sufficiently small sieve cutoff is still required.

## 1. CRT completion thins the mixed Fourier support to `p` modes

The function

\[
F_{q,a}(n)=K_h(n)e(an/q)
\]

is periodic modulo `pq`. Let its complete Fourier coefficient at `r (mod pq)` be

\[
\widehat F_{q,a}(r)
=\sum_{n\bmod pq}F_{q,a}(n)e(-rn/(pq)).
\tag{7}
\]

Under the Chinese remainder isomorphism

\[
\mathbf Z/(pq)\mathbf Z
\cong
\mathbf Z/p\mathbf Z\times\mathbf Z/q\mathbf Z,
\]

the `q`-coordinate sum is

\[
\sum_{v\bmod q}e_q\!\left((a-rp^{-1})v\right).
\tag{8}
\]

It vanishes unless

\[
r\equiv ap\pmod q.
\tag{9}
\]

Write every surviving frequency uniquely as

\[
r=ap+kq\pmod{pq},\qquad k\bmod p.
\tag{10}
\]

The `q`-sum in `(8)` then equals `q`, while the remaining `p`-factor is, after harmless reindexing of `k`,

\[
C_h(k):=
\sum_{u\bmod p}K_h(u)e_p(-ku).
\tag{11}
\]

Hence the only nonzero complete coefficients are

\[
\widehat F_{q,a}(ap+kq)=q\,C_h(k).
\tag{12}
\]

This exact support thinning is the source of the denominator independence. Fourier inversion on an interval gives, up to reindexing signs,

\[
S_{q,a}(I)
=
\frac1p\sum_{k\bmod p}
C_h(k)
D_I\!\left(\frac aq+\frac kp\right),
\tag{13}
\]

where

\[
D_I(\theta)=\sum_{n\in I}e(n\theta).
\]

For `k=0`, the complete translated-character correlation is exactly `C_h(0)=-1`. For `k!=0`, `(11)` is a bounded-complexity mixed additive--multiplicative character sum with rational multiplicative phase `(u+h)/u`. The classical Weil estimate gives

\[
|C_h(k)|\ll\sqrt p
\tag{14}
\]

uniformly in nonzero `h`; enlarging the constant makes `(14)` valid for all `k`.

Finally, for every `H<=p` and every real shift `theta`, the standard Dirichlet-kernel grid estimate gives

\[
\sum_{k\bmod p}|D_I(\theta+k/p)|
\ll p\log(2p).
\tag{15}
\]

Combining `(13)`--`(15)` proves `(2)`. The argument is simply completion plus the complete mixed Weil bound; no RH-scale or zero-free input is present.

## 2. The Bera--Viswanadham coefficient envelope costs at most `z^3/G(z)` by `ell^1`

Bera and Viswanadham's Section 3 imports the Ramaré--Ruzsa enveloping sieve and writes its weight as

\[
\beta(n)=
\sum_{\substack{q\le z^2\\q\mid P(2,z)}}
\sum_{a\bmod q}^{*}
w(a/q)e(an/q).
\tag{16}
\]

In the dimension-two pair-sieve application of `MC-476`, each small prime excludes one or two residues. With `z_0=2`, the finite prefactor over primes below `z_0` in Bera--Viswanadham Lemma 3.2 is empty, so their coefficient estimate specializes to `(3)` with an absolute line-level constant.

Using only `phi(q)<=q`,

\[
\sum_{q\le z^2}\frac{\varphi(q)}{\sqrt q}
\le
\sum_{q\le z^2}\sqrt q
\ll z^3.
\tag{17}
\]

Insert `(2)` into `(16)` and sum coefficients absolutely. Equations `(3)` and `(17)` give `(5)`.

The `z^3` factor is an **upper bound for this crude coefficientwise recombination**, not a lower bound or an unavoidable barrier. The actual coefficients have arithmetic structure and much smaller support than all rational points of height `z^2`; exploiting that structure is precisely one remaining way to improve `(5)`.

## 3. Plain `ell^2` closure removes the cubic coefficient cost but also removes the conductor gain

The opposite generic endpoint does not solve the problem. Put `Q=z^2`. The additive large sieve for reduced rational frequencies gives

\[
\sum_{q\le Q}\sum_{a\bmod q}^{*}
|S_{q,a}(I)|^2
\ll (H+Q^2)
\sum_{n\in I}|K_h(n)|^2.
\tag{18}
\]

Since `|K_h(n)|<=1`, and in the restriction range `z<=H^{1/4}` one has `Q^2=z^4<=H`, the right side is `O(H^2)`. On the coefficient side, `(3)` gives

\[
\sum_{q\le z^2}\sum_{a\bmod q}^{*}|w(a/q)|^2
\ll
\frac1{G(z)^2}
\sum_{q\le z^2}\frac{\varphi(q)}q
\ll
\frac{z^2}{G(z)^2}.
\tag{19}
\]

Cauchy--Schwarz therefore yields only

\[
\left|\sum_{n\in I}K_h(n)\beta(n)\right|
\ll \frac{Hz}{G(z)},
\tag{20}
\]

which contains no negative power of `p`. Thus the two naive norm closures expose a real tradeoff: coefficientwise `ell^1` preserves the complete-character square-root gain but pays `z^3`, whereas generic `ell^2` controls the rational-frequency family collectively but forgets the conductor-sensitive cancellation.

This does not prove that every interpolation or structured bilinear treatment must fail. It identifies the next target more sharply: any improvement should exploit joint arithmetic structure of `w(a/q)` and the CRT-thinned character transforms rather than using only their separate `ell^1` or `ell^2` norms.

## 4. The exact pair-sieve replacement remains the decisive unresolved step

The original rough×rough object is

\[
\sum_{n\in I}K_h(n)A_{W,h}(n),
\qquad
A_{W,h}(n)=\mathbf 1_{(n(n+h),W)=1},
\]

not the envelope sum in `(5)`. A pointwise inequality such as `A<=beta` does not imply

\[
\left|\sum K_h A\right|
\le
\left|\sum K_h\beta\right|.
\]

The phase of `K_h` makes that inference invalid. Consequently `MC-477` settles only the first half of the decisive test stated in the accepted clue: **the rational-frequency family itself admits a conductor-sensitive estimate with an explicit polynomial aggregate cost.** It does not settle the signed approximation/replacement error.

A successful continuation must therefore do at least one of the following without reverting to the closed full-primorial routes:

- exploit arithmetic cancellation among the coefficients `w(a/q)` strongly enough to improve the crude `z^3` recombination while retaining the `sqrt(p)` source gain;
- place the exact indicator and envelope inside a legitimate positive quadratic form that retains useful `K_h` information; or
- directly control the signed difference `sum K_h(A-beta)` on the actual source interval.

If none of these can be done below the conductor-saving budget, then the compressed representation is analytically cheaper than the hard mask but still insufficient for the original pair-sieve sum.

## Prior art and novelty boundary

Tanmoy Bera and G. K. Viswanadham, *Restriction estimates with sifted integers*, arXiv:2512.21640v3 (revised 13 May 2026), Section 3 and Lemmas 3.1--3.2, provide the enveloping-sieve rational Fourier representation with denominators `q<=z^2` and the `q^(-1/2)/G(z)` coefficient bound used in `(16)`--`(19)`. Their Section 3 explicitly attributes the enveloping-sieve input to Section 4 of Olivier Ramaré and Imre Z. Ruzsa, *Additive properties of dense subsets of sifted sequences*, Journal de Théorie des Nombres de Bordeaux 13 (2001), 559--581, DOI `10.5802/jtnb.338`.

The complete finite-field estimate `(14)` is classical. Todd Cochrane and Christopher Pinner, *Using Stepanov's method for exponential sums involving rational functions*, Journal of Number Theory 116 (2006), 270--292, DOI `10.1016/j.jnt.2005.04.001`, supplies the relevant Weil-type bound for mixed additive and multiplicative character sums of rational functions and is already registered as `MC-S55`.

The CRT factorization, support thinning, interval completion, rational-frequency large sieve, and coefficient aggregation above are elementary/classical analytic-number-theory operations. A targeted prior-art check on 23 September 2026 found no basis for claiming a new character-sum theorem. No novelty is claimed for `(2)` or `(5)`. The durable Mathia contribution is the candidate-specific accounting: in the exact `MC-476` source frame, the low-denominator envelope avoids the full primorial frequency dimension, each rational denominator disappears from the completed character estimate, and the remaining naive tradeoff is explicitly `z^3` versus loss of conductor sensitivity under `ell^2` closure.

## Boundaries and falsification tests

- **`h not congruent 0 (mod p)` is essential.** If `h=0 (mod p)`, the translated ratio degenerates and the character correlation need not cancel. Such shifts must be isolated rather than passed through `(14)`.
- **`(q,p)=1` is essential to the clean CRT factorization.** It holds for the `MC-476` envelope because the source-conductor prime is excluded from the sieve product. A representation that reintroduces `p` into the rational denominator requires a separate local calculation.
- **The interval length is at most one source conductor block.** Equation `(15)` is used for `H<=p`. Longer intervals should first separate complete `p`-blocks and their exact mean.
- **The `z^3` factor is method-specific.** It comes from summing the pointwise coefficient bounds absolutely over all admissible rational frequencies. It is not asserted to be sharp.
- **The large-sieve endpoint is also method-specific.** Equation `(20)` shows only that plain Cauchy--Schwarz plus the standard additive large sieve loses the conductor gain; it does not exclude a structured hybrid estimate.
- **No signed replacement theorem is proved.** The envelope estimate cannot be transferred to the exact rough×rough indicator by positivity alone.
- **The restriction admissibility `z<=H^(1/4)` and the conductor-saving requirement `(6)` are independent.** Satisfying the former does not imply the latter.
- **No Möbius, Mertens, zero-free, or RH consequence follows.** This is a source-kernel estimate inside one staged sieve component.

## Consequence for the research line

`MC-473` showed that exact pair-sieve inclusion-exclusion followed by independent completion pays exponentially many branches; `MC-474` converted the same obstruction into exponential hard-mask Fourier `ell^1` mass; `MC-475` showed that full-grid Parseval pays the primorial frequency dimension; and `MC-476` showed that the current coefficient-uniform sifted restriction theorem is blind to the special character coefficient at zero frequency.

The low-denominator representation now survives one more serious test. Its individual rational modes are analytically benign: after CRT completion they cost `sqrt(p) log p` independently of denominator, and crude recombination costs only `z^3/G(z)`, not the full primorial dimension. But that does not yet close the actual rough×rough problem. The next decisive question is no longer whether rational-frequency character sums can be bounded; it is whether the envelope coefficients or the signed exact-to-envelope replacement can be handled **without sacrificing the conductor gain that `(2)` exposes**.