# MC-344 — Bit-flip source readout has a linear Shannon-capacity threshold

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-340` shows that bounded-energy dephasing of the reciprocal endpoint requires a transcript carrying a linear amount of information about the joint source vector. `MC-343` prices that requirement for a fixed-dimensional Gaussian analog readout. A different source-natural model is to expose noisy source coordinates themselves.

Keep the source law of `MC-340`:

\[
G=\mathbf F_2^R,\qquad \Xi=G\setminus\{0\},\qquad m=2^R-1,
\]

with `A` uniform on `Xi` and

\[
X=(X_1,\ldots,X_R)\in\{-1,+1\}^R.
\]

Choose a coordinate set `J\subseteq[R]`, `|J|=k`, and pass the selected source phases independently through a binary symmetric channel with crossover probability `q\in[0,1/2]`:

\[
Z_j=X_jN_j,\qquad
\mathbf P(N_j=-1)=q,
\qquad j\in J,
\tag{1}
\]

where the `N_j` are independent of each other and of `X`. Allow arbitrary downstream postprocessing `X\to Z_J\to Y`. With natural logarithms define

\[
h(q)=-q\log q-(1-q)\log(1-q),
\qquad
c(q)=\log2-h(q).
\tag{2}
\]

Then, without any independence assumption on the coordinates of `X`,

\[
\boxed{
I(X;Y)\le I(X;Z_J)\le k\,c(q).
}
\tag{3}
\]

Combining `(3)` with the global transcript obstruction of `MC-340` gives the exact capacity requirement

\[
\boxed{
k\,c(q)
\ge
\frac R2
\left(\frac{\eta^2}{C}-\frac1{m^2}\right)
-\operatorname{TC}(X)
}
\tag{4}
\]

whenever the normalized coefficient energy satisfies `\mathcal E(W)\le C` and the all-mode dephasing error satisfies `\delta(W)\le1-\eta`. Since `\operatorname{TC}(X)=O(1)`, fixed `C,eta>0` force

\[
\frac{k}{R}
\ge
\frac{\eta^2}{2C\,c(q)}+o(1)
\tag{5}
\]

whenever `c(q)>0`.

Thus bounded-energy constant-factor dephasing through a bit-flip source readout needs **linear source-coordinate bandwidth** unless the channel is nearly noiseless enough to compensate. Conversely, fixed positive bit-flip noise does not by itself create the fixed-dimensional bottleneck of `MC-343`: if `k\asymp R` and `q<1/2` is fixed, the channel still has `Theta(R)` information capacity.

At the matched-filter energy floor the threshold sharpens. If

\[
\mathcal E(W)\le1,
\qquad
\delta(W)\le\varepsilon,
\qquad
\alpha_\varepsilon:=\varepsilon-\frac{\varepsilon^2}{2},
\tag{6}
\]

then `MC-340` gives

\[
I(X;Y)\ge H(X)-R h(\alpha_\varepsilon).
\]

For full coordinate readout `k=R`, `(3)` therefore implies

\[
h(q)\le h(\alpha_\varepsilon)+o(1).
\tag{7}
\]

For fixed `q\in[0,1/2]`, monotonicity of binary entropy yields

\[
\boxed{
\varepsilon
\ge
1-\sqrt{1-2q}+o(1).
}
\tag{8}
\]

So any fixed nonzero crossover rate imposes a fixed positive near-exact dephasing floor at unit energy. Exact dephasing is impossible for `q>0` in this readout model.

The reciprocal source law permits a sharper matched-control statement. For **full** readout `J=[R]`, write `M=2^R`, `r=1-2q`, and

\[
b=q^2+(1-q)^2=\frac{1+r^2}{2}.
\]

If `U_R` is the uniform law on `\{-1,+1\}^R`, then

\[
\boxed{
I(X;Z)=R c(q)-D(P_Z\|U_R).
}
\tag{9}
\]

For even `R`,

\[
\boxed{
\chi^2(P_Z\|U_R)
=
\frac{M b^R-1}{(M-1)^2}.
}
\tag{10}
\]

For odd `R`,

\[
\boxed{
\chi^2(P_Z\|U_R)
=
\frac{M(M-2)r^{2R}+M b^R-1}{(M-1)^2}.
}
\tag{11}
\]

Since

\[
0\le D(P_Z\|U_R)\le\log\bigl(1+\chi^2(P_Z\|U_R)\bigr),
\tag{12}
\]

for every fixed `q\in(0,1/2]`,

\[
\boxed{I(X;Z)=R c(q)-o(1).}
\tag{13}
\]

Therefore the puncturing and odd-rank parity dependence of the reciprocal source vector do **not** create an additional extensive capacity loss under fixed positive bit-flip noise. A full source-coordinate BSC asymptotically saturates the ordinary BSC capacity. For odd `R`, the extra term `r^{2R}` in `(11)` also identifies the parity-memory washout scale: the one-bit parity constraint disappears when `Rq\to\infty`, while it survives when `q=o(1/R)`.

This closes one ambiguity left by `MC-343`: positive readout noise is not by itself a universal obstruction. The decisive resource is aggregate channel capacity. To rule out a source-natural discrete readout one must prove that only `o(R)` source coordinates are exposed, that their effective crossover rates approach `1/2` fast enough that total capacity is `o(R)`, or that the actual arithmetic channel has another structural restriction reducing its joint capacity.

No estimate for `M(x)` follows.

## 1. Capacity bound for an arbitrary dependent source

Conditioned on the complete source vector `X`, the selected output coordinates are independent BSC flips, so

\[
H(Z_J\mid X)=k h(q).
\tag{14}
\]

The output alphabet has `2^k` elements, hence

\[
H(Z_J)\le k\log2.
\tag{15}
\]

Therefore

\[
I(X;Z_J)
=H(Z_J)-H(Z_J\mid X)
\le k(\log2-h(q))
=k c(q).
\tag{16}
\]

Data processing through `X\to Z_J\to Y` proves `(3)`. This is the ordinary binary-symmetric-channel capacity converse specialized to an arbitrary, possibly dependent, source law; no source-coordinate independence is used.

Now `MC-340` proves that `\mathcal E(W)\le C` and `\delta(W)\le1-\eta` require

\[
I(X;Y)
\ge
\frac R2
\left(\frac{\eta^2}{C}-\frac1{m^2}\right)
-\operatorname{TC}(X).
\tag{17}
\]

Combining `(16)` and `(17)` gives `(4)`. The explicit entropy calculation in `MC-340` gives `\operatorname{TC}(X)\to0` for even `R` and `\operatorname{TC}(X)\to\log2` for odd `R`, proving `(5)`.

For full readout one can also insert `I(X;Y)\le R c(q)` directly into the lower bound of `MC-340` to obtain

\[
\delta(W)
\ge
\left(
1-\sqrt C\sqrt{
\frac1{m^2}+2c(q)+\frac{2\operatorname{TC}(X)}R
}
\right)_+.
\tag{18}
\]

As `q\to1/2`, `c(q)\to0`, so the lower bound tends to one for fixed `C`: nearly random source bits cannot support fixed dephasing even when every coordinate is observed.

## 2. Unit-energy near-exact dephasing pays the BSC entropy loss

At `\mathcal E(W)\le1`, `MC-340` gives the stronger Fano-based requirement

\[
I(X;Y)
\ge
H(X)-R h(\alpha_\varepsilon).
\tag{19}
\]

For full readout, `(3)` and `(19)` imply

\[
R(\log2-h(q))
\ge
H(X)-R h(\alpha_\varepsilon).
\tag{20}
\]

The exact reciprocal source entropy from `MC-340` satisfies

\[
H(X)=R\log2-O(1).
\tag{21}
\]

Dividing `(20)` by `R` gives `(7)`. On `[0,1/2]`, `h` is increasing. For the relevant `\varepsilon\in[0,1]`, `\alpha_\varepsilon\in[0,1/2]`, hence `(7)` gives

\[
\alpha_\varepsilon\ge q-o(1).
\]

Solving `\varepsilon-\varepsilon^2/2\ge q` on `[0,1]` yields `(8)`.

For exact error `\varepsilon=0`, the stronger conclusion does not require an asymptotic argument. If `q\in(0,1/2]`, every BSC output word has positive probability under every source word, so no postprocessing of `Z` can determine `X` exactly. But exact unit-energy dephasing in `MC-340` forces `H(X\mid Y)=0`. These two statements are incompatible.

## 3. Exact output law for the reciprocal source vector

The source dependence can be priced rather than hidden behind the generic capacity bound.

For even `R`, `MC-340` shows that `X` is uniform on the full cube with the all-`+1` word `x_0` removed. Let

\[
a_z:=\mathbf P(Z=z\mid X=x_0)
=q^{d(z,x_0)}(1-q)^{R-d(z,x_0)}.
\]

Because the BSC is doubly stochastic, summing its transition probabilities over all `M` possible inputs gives one for each fixed output. Removing `x_0` therefore gives

\[
P_Z(z)=\frac{1-a_z}{M-1}.
\tag{22}
\]

Using `\sum_z a_z=1` and

\[
\sum_z a_z^2=(q^2+(1-q)^2)^R=b^R
\tag{23}
\]

in the definition of chi-square divergence from the uniform law gives `(10)` exactly.

For odd `R`, the source-character map has image the even-parity subgroup. The all-`+1` word has source probability `1/(M-1)` and every other even-parity word has probability `2/(M-1)`. Writing

\[
s(z):=\prod_{i=1}^R z_i\in\{-1,+1\},
\]

this source law is the even-parity uniform weight minus one copy of the all-`+1` atom. Under the BSC,

\[
P_Z(z)
=
\frac{1+s(z)r^R-a_z}{M-1}.
\tag{24}
\]

The identities

\[
\sum_z s(z)=0,
\qquad
\sum_z s(z)a_z=r^R,
\qquad
\sum_z a_z^2=b^R
\tag{25}
\]

then give `(11)` by direct expansion.

Finally,

\[
H(Z)=R\log2-D(P_Z\|U_R),
\]

and `H(Z\mid X)=Rh(q)`, proving `(9)`. The standard inequality `D(P\|Q)\le\log(1+\chi^2(P\|Q))` gives `(12)`. For fixed `q>0`, both `|r|<1` and `b<1`, and `(10)`–`(11)` make the divergence correction exponentially small, proving `(13)`.

The odd-rank term is especially diagnostic. Its leading nonuniformity is `r^{2R}`. Since `r=1-2q`, for small `q` one has `r^{2R}=\exp(-4Rq+O(Rq^2))`. Hence `Rq` is the natural threshold for washing out the one exact parity relation inherited from the noiseless odd-rank source law.

## Prior art and novelty boundary

The information-theoretic channel mechanism is classical. Cover and Thomas, *Elements of Information Theory*, 2nd ed., Chapter 7, “Channel Capacity”, Wiley, DOI `10.1002/047174882X.ch7`, includes the binary symmetric channel and its capacity `1-H_2(q)` bits per use, together with the channel-capacity converse and data-processing framework used in `(3)`.

Entropy of dependent binary vectors after independent bit-flip noise is also an established subject. Alex Samorodnitsky, *On the Entropy of a Noisy Function*, IEEE Transactions on Information Theory **62** (2016), 5446–5464, DOI `10.1109/TIT.2016.2584625`, develops a strengthening of Mrs. Gerber's lemma for binary vectors passed through a BSC. A targeted literature audit on 17 September 2026 therefore treats the BSC capacity and noisy-Boolean-vector entropy theory as prior art, not as Mathia novelty.

No standalone novelty claim is made. The durable line-specific delta is the exact coupling of that classical capacity to the independent `MC-340` dephasing-information lower bound, plus the closed-form punctured/parity source corrections `(10)`–`(13)`. Those formulas show that the reciprocal endpoint source dependence costs only a vanishing capacity correction under fixed positive bit-flip noise, so an extensive discrete readout is a genuine matched escape from the fixed-dimensional Gaussian obstruction of `MC-343`.

## Boundaries and falsification tests

- **The BSC is a readout model, not an arithmetic theorem.** Nothing here proves that a natural Möbius-derived statistic exposes source phases through independent bit flips with any particular `q`.
- **Independent flips are load-bearing for the exact channel formulas.** Correlated or source-dependent noise can have a different aggregate capacity and must be priced separately.
- **The generic upper bound `(3)` does not require independent source coordinates.** All reciprocal source dependence is permitted; only the channel noise is independent conditional on `X`.
- **Fixed positive noise does not imply sublinear information.** With `k=Theta(R)` and fixed `q<1/2`, equation `(13)` shows `Theta(R)` information survives. Any argument that says merely “the readout is noisy” is therefore insufficient.
- **Near-random noise is different.** If `c(q_R)=o(1)` and `k\le R`, total capacity is `o(R)` and `MC-340` forbids fixed constant-factor bounded-energy dephasing.
- **The parity washout threshold is source-specific.** The `Rq` scale comes from the single odd-rank parity relation of this reciprocal endpoint law; it is not asserted for arbitrary binary sources.
- **Exact dephasing impossibility at `q>0` uses overlapping channel support.** It does not extend automatically to erasure or noiseless-but-quantized channels, which require their own capacity audit.
- **No RH or Mertens estimate follows.** This is a finite reciprocal-endpoint admission theorem refining which transcript architectures can or cannot carry the information demanded by `MC-340`.

## Consequence for the research line

`MC-341`–`MC-343` show that low state count, fixed-dimensional bounded spread, forward regularity without inverse control, and fixed-dimensional Gaussian readout all fail to carry enough source information cheaply. The BSC calculation separates a different regime: **extensive source bandwidth can defeat the noise obstruction**.

Accordingly the next arithmetic question is not whether a proposed transcript is merely noisy. It is whether its *aggregate source capacity* is sublinear. A viable obstruction must derive one of three genuinely source-dependent facts: fewer than linearly many independently informative source degrees of freedom, crossover/noise strong enough that capacity per degree of freedom vanishes, or structural dependence that makes the total channel capacity much smaller than the sum of its apparent coordinate capacities. Without such a theorem, a linear-width noisy digital transcript remains compatible with the information demanded by bounded-energy endpoint dephasing.