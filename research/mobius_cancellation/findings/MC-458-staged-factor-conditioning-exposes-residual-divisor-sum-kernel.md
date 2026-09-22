# MC-458 — Staged factor conditioning exposes a residual divisor-sum kernel before product collapse

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `CANDIDATE-NEW-STRUCTURE` · `FRONTIER-ADVANCE` · `PRE-POSITIVE-FACTOR-SEPARATION` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The live branch after `MC-454`--`MC-457` asks whether a genuine well-factorable decomposition can be used **before** the internal factors collapse to the product-indexed translated-character kernel. There is an exact staging in which one factor block remains visible in the source-dependent kernel without introducing it merely as an independent coprime residue mask.

Let

\[
\lambda=\alpha*\beta,
\qquad
\lambda_d=\sum_{rs=d}\alpha_r\beta_s,
\tag{1}
\]

and define the residual divisor-sum weight

\[
B_\beta(y):=\sum_{s\mid y}\beta_s.
\tag{2}
\]

For

\[
w(m):=\sum_{d\mid m}\lambda_d,
\tag{3}
\]

finite rearrangement gives the exact identity

\[
\boxed{
w(m)=\sum_{r\mid m}\alpha_r B_\beta(m/r).
}
\tag{4}
\]

Hence the shifted correlation from `MC-413`, with

\[
F_h(n):=\chi(n+h)\overline{\chi(n)},
\tag{5}
\]

can be regrouped as

\[
\boxed{
C_h(N)
=\sum_{r,r'}\alpha_r\overline{\alpha_{r'}}
\sum_{\substack{n\le N-h\\ r\mid n+h\\ r'\mid n}}
F_h(n)
B_\beta((n+h)/r)
\overline{B_\beta(n/r')}.
}
\tag{6}
\]

This is not yet the product pullback `K_h(rs,r's')` of `MC-454`. One factor block `(r,r')` determines the progression on which the source character is sampled, while the complementary factor block remains inside two residual divisor-sum weights evaluated along quotient progressions.

If `(r,r')\mid h` and `(rr',q)=1`, set `R=[r,r']` and choose the CRT class `a (mod R)` with

\[
a\equiv-h\pmod r,
\qquad
a\equiv0\pmod{r'}.
\tag{7}
\]

Writing `n=a+Rk`, define the integers

\[
A_r=(a+h)/r,
\qquad
A_{r'}=a/r',
\qquad
v_r=R/r,
\qquad
v_{r'}=R/r',
\tag{8}
\]

and the source residues

\[
u\equiv aR^{-1}\pmod q,
\qquad
\delta\equiv hR^{-1}\pmod q.
\tag{9}
\]

Then the inner kernel in `(6)` is exactly

\[
\boxed{
\sum_{k\in I_{r,r'}}
\chi(k+u+\delta)\overline{\chi(k+u)}
B_\beta(A_r+v_r k)
\overline{B_\beta(A_{r'}+v_{r'}k)}.
}
\tag{10}
\]

Equation `(10)` is the first exact object in this branch in which an internal well-factorable block survives as more than a repeated label of the same product-level source sample. The residual `B_\beta` factors are generally neither constant nor `q`-periodic independent masks, so the complete-block CRT tensorization of `MC-457` does not apply to `(10)` as stated.

The gain is only **structural at this stage**. Expanding both copies of `B_\beta` in `(10)` restores the complementary divisors `s,s'` and recovers exactly the original product variables `d=rs`, `e=r's'` of `MC-413`. Thus no arithmetic information has been created. What has changed is the order in which the same information is exposed to analysis: `(10)` gives a legitimate window in which the `r`-block can interact with the source while the complementary `s`-block is still retained as a divisor-sum amplitude, before multiplication quotienting or positive closure.

There is also a useful exact size baseline for the residual weight. If `|\beta_s|\le1` and `\beta_s=0` for `s>S`, then for every `Y\ge1`,

\[
\sum_{y\le Y}|B_\beta(y)|^2
=\sum_{s,t\le S}\beta_s\overline{\beta_t}
\left\lfloor\frac{Y}{[s,t]}\right\rfloor,
\tag{11}
\]

and therefore

\[
\boxed{
\sum_{y\le Y}|B_\beta(y)|^2
\ll Y(1+\log S)^3.
}
\tag{12}
\]

So retaining the complementary factor block through `B_\beta` does not, in an unrestricted average, carry an unavoidable polynomial `L^2` penalty. This does **not** yet control `(10)`: the affine quotient progressions can be arithmetically biased with respect to the divisibility structure of `B_\beta`, and the character phase must be estimated jointly with both residual weights.

Consequently `MC-457` does not establish a global no-go for all pre-positive factor-specific orderings. It closes the ordering in which a factor is kept only as an independent coprime residue condition and the source is then fully completed. The staged divisor-sum ordering `(4)`--`(10)` lies outside that hypothesis. The decisive remaining question is quantitative: can `(10)` be estimated collectively, before expanding `B_\beta` or applying separate positive bounds, with a strict conductor-power gain after its true diagonal and progression concentration are charged?

No improved bound for `M(x)`, no character-sum exponent, no zero-free region, and no RH consequence follows.

## 1. Exact staged factorization

Starting from `(1)` and `(3)`,

\[
\begin{aligned}
w(m)
&=\sum_{d\mid m}\sum_{rs=d}\alpha_r\beta_s\\
&=\sum_{rs\mid m}\alpha_r\beta_s\\
&=\sum_{r\mid m}\alpha_r
   \sum_{s\mid m/r}\beta_s,
\end{aligned}
\tag{13}
\]

which proves `(4)`.

Substituting `(4)` into

\[
C_h(N)=\sum_{n\le N-h}w(n+h)\overline{w(n)}F_h(n)
\tag{14}
\]

and exchanging finite sums yields `(6)`. The simultaneous congruences in `(6)` are soluble exactly when `(r,r')\mid h`. If a prime dividing the primitive conductor `q` divides `r`, then `r\mid n+h` forces `\chi(n+h)=0`; if it divides `r'`, then `\chi(n)=0`. Hence only `(rr',q)=1` contributes, just as in the product-level expansion.

For a contributing pair, the admissible integers form one residue class `(7)` modulo `R=[r,r']`. Substitution `n=a+Rk` gives

\[
(n+h)/r=A_r+v_rk,
\qquad
n/r'=A_{r'}+v_{r'}k.
\tag{15}
\]

Because `R` is invertible modulo `q`, the character phase rescales as

\[
F_h(a+Rk)
=
\chi(k+u+\delta)\overline{\chi(k+u)},
\tag{16}
\]

with `(9)`, proving `(10)`.

The important asymmetry is now explicit. The `r`-variables control the congruence class, interval geometry, quotient slopes `v_r,v_{r'}`, and source translation through `R`; the complementary `s`-variables remain inside `B_\beta`. That distinction exists only while the convolution is staged.

## 2. Expansion recovers the old product quotient exactly

The staged kernel is not new arithmetic data. Expanding the first residual weight gives

\[
B_\beta((n+h)/r)
=
\sum_{s\mid(n+h)/r}\beta_s
=
\sum_{s:\,rs\mid n+h}\beta_s,
\tag{17}
\]

and similarly

\[
\overline{B_\beta(n/r')}
=
\sum_{s':\,r's'\mid n}\overline{\beta_{s'}}.
\tag{18}
\]

Substituting `(17)`--`(18)` into `(6)` gives

\[
\sum_{r,s,r',s'}
\alpha_r\beta_s\overline{\alpha_{r'}\beta_{s'}}
\sum_{\substack{n\le N-h\\rs\mid n+h\\r's'\mid n}}F_h(n),
\tag{19}
\]

which is precisely the `d=rs`, `e=r's'` form of `MC-413`/`MC-454`.

This identifies the exact resource and its exact failure mode. If a proof expands `(17)`--`(18)` before obtaining a useful estimate, or bounds the residual divisor sums separately by absolute values in a way that forgets their coupling to `k`, it returns to the already-classified product/lcm source frame. Any benefit from well-factorability must be extracted **between** `(10)` and `(19)`.

This is analogous in role, though not yet in strength, to the successful dispersion architectures audited in `MC-456`: the internal factors matter only because the proof acts while different factor blocks still occupy different analytic roles. Here the distinct roles are a progression-conditioning block and a residual divisor-sum block, rather than separate factors of one arithmetic-progression modulus.

## 3. The residual divisor sum has only polylogarithmic unrestricted second moment

Equation `(11)` follows by expanding the square and counting common multiples:

\[
\begin{aligned}
\sum_{y\le Y}|B_\beta(y)|^2
&=\sum_{s,t\le S}\beta_s\overline{\beta_t}
\#\{y\le Y:s\mid y,\ t\mid y\}\\
&=\sum_{s,t\le S}\beta_s\overline{\beta_t}
\left\lfloor\frac{Y}{[s,t]}\right\rfloor.
\end{aligned}
\tag{20}
\]

For `|\beta_s|\le1`,

\[
\sum_{y\le Y}|B_\beta(y)|^2
\le
Y\sum_{s,t\le S}\frac1{[s,t]}.
\tag{21}
\]

Using

\[
\frac1{[s,t]}=\frac{(s,t)}{st},
\qquad
(s,t)=\sum_{d\mid(s,t)}\varphi(d),
\tag{22}
\]

we obtain the exact positive rearrangement

\[
\sum_{s,t\le S}\frac1{[s,t]}
=
\sum_{d\le S}rac{\varphi(d)}{d^2}
H_{\lfloor S/d\rfloor}^2,
\tag{23}
\]

where `H_m=\sum_{j\le m}1/j`. Since `\varphi(d)/d^2\le1/d` and `H_m\le1+\log m`, the right side is `O((1+\log S)^3)`, proving `(12)`.

This estimate matters only as a baseline. It says that the residual block is not automatically too large in a global mean square. It does **not** prove a corresponding estimate after restricting `y` to the affine forms in `(15)`. A step such as `v_r=R/r` can share primes with the residual divisors and create concentrated divisibility patterns. Any use of `(12)` inside `(10)` must therefore be replaced by, or derived into, a progression-sensitive estimate for the actual family.

## 4. Why `MC-457` does not tensorize this kernel

`MC-457` considers a `q`-periodic source function `F` multiplied by an **independent coprime residue mask** modulo `r`. Over a complete mixed `qr` block, CRT separates the coordinates: nonzero factor frequencies vanish and the surviving source average is the universal complete `q`-sum.

Equation `(10)` has a different structure. After the `r,r'` congruences have been solved, the summand is

\[
F_{u,\delta}(k)
\,B_\beta(A_r+v_rk)
\,\overline{B_\beta(A_{r'}+v_{r'}k)}.
\tag{24}
\]

The second and third factors vary with the **same integer `k`** as the translated character. They are not, without further expansion, a function of an independent CRT coordinate. A complete `q`-block in `k` therefore cannot be replaced by `c_q(h)` unless one has first shown that the residual weights decouple appropriately; in general they do not even have period `q`.

Thus the fixed external conductor does not by itself force every staged factorable representation to tensorize before the first estimate. What `MC-457` proves remains exact: if the retained factor enters only as a coprime congruence mask and the rest of the summand is `q`-periodic, full completion kills that factor mode. The residual-divisor-sum carrier evades precisely that premise.

This is a useful correction to the strongest possible negative reading of the preceding frontier. It does not establish that `(24)` is easier than the expanded product-level form; only a quantitative dispersion estimate can decide that.

## 5. Prior art and novelty boundary

The convolution regrouping `(13)`, divisor-sum expansion `(20)`, gcd identity `(22)`, and harmonic bound in `(23)` are elementary/classical. No novelty is claimed for any of them.

The analytic principle that well-factorable weights become useful when their convolution variables are exposed before Cauchy/dispersion/positive closure is established prior art. `MC-453` audits the bounded Iwaniec linear-sieve decomposition and modern well-factorable use; `MC-456` audits a stronger current example in Pascadi's triply-well-factorable dispersion and Yang's 2026 convolution-type Bombieri--Vinogradov theorem. A fresh check of the primary records on 22 September 2026 also confirms Maynard's well-factorable large-modulus theorem, Pascadi's `5/8-o(1)` triply-well-factorable theorem, and Yang's explicit use of Pascadi's convolution/incomplete-Kloosterman machinery. These works justify the neighboring analytic language but do not estimate `(10)`.

The durable Mathia delta is narrower: for the exact shifted Möbius source form already isolated in this line, `(4)`--`(10)` give a concrete legal ordering in which one factor block remains analytically visible and the simple CRT tensorization of `MC-457` no longer applies. This is a branch-specific representation result, not a claim that staged divisor sums are new or that the resulting estimate is known to improve classical bounds.

## Boundaries and falsification tests

- **No power saving has been proved.** The finding supplies a carrier and a global size baseline, not an estimate for the weighted translated-character family `(10)`.
- **Expansion kills the staging advantage.** Expanding both `B_\beta` factors before the decisive oscillatory estimate restores `(19)` and hence the product-level quotient of `MC-454`.
- **Absolute majorization may kill it just as effectively.** A bound that replaces both residual weights by independent absolute divisor bounds before using the character phase can recreate the old occupancy/diagonal loss even without writing `(19)` explicitly.
- **The progression-sensitive `L^2` problem is load-bearing.** The unrestricted estimate `(12)` is not transferable for free to `B_\beta(A+vk)`, because divisibility can correlate strongly with the step `v` and offset `A`.
- **Degenerate residual blocks give no separation.** If `\beta` is concentrated at `1`, or `B_\beta` is constant on the relevant progression, `(10)` reduces to the translated-character family already classified by `MC-413`--`MC-457`.
- **Coprimality with the source conductor remains load-bearing.** Terms with `(rr',q)>1` vanish before the staged analysis. A future representation that shares useful modulus factors with the primitive conductor lies outside this exact setup and must first evade that vanishing.
- **The external-conductor mismatch remains real.** Unlike Pascadi/Yang, the factor block here is not itself a factor of the character conductor. The new coupling is through the quotient divisor weights, not a reciprocal phase in a shared modulus. Its analytic strength must be proved rather than inferred by analogy.
- **No zeta continuation is used.** Everything through `(24)` is finite convolution/divisor algebra plus the primitive-character rescaling already present in `MC-413`.

## Consequence for the research line

The accepted factor-specific-dispersion clue has passed one structural admission test but not its quantitative test. There **is** a legal pre-positive ordering that avoids immediate multiplication collapse: expose one factor block as the progression condition and leave the complementary block inside the residual divisor-sum weights `(10)`. The strongest possible claim that the fixed external conductor forces every factorable ordering to become product/lcm-level before analysis is therefore false.

The next decisive object is now concrete. For balanced well-factorable ranges, estimate the family

\[
\sum_{k\in I}
\chi(k+u+\delta)\overline{\chi(k+u)}
B_\beta(A+vk)\overline{B_\beta(A'+v'k)}
\tag{25}
\]

**before** expanding the residual divisor sums and before componentwise positive closure. Compute its true diagonal and progression-sensitive second moment, then propagate the result through the source-depth/occupancy budget of `MC-415`/`MC-448`. A strict conductor-power gain would turn the staged carrier into a real mechanism; a theorem showing that every admissible estimate of `(25)` necessarily pays the old product-level tariff would close this escape cleanly.