# VIS-108 — an exact Markov-type chronology pair is Fourier-homometric

## Claim

There exist two binary words in the **same exact order-three Markov type** whose ordinary three-delay path signatures differ at degree four, but whose complete one-dimensional Fourier magnitudes are identical at every frequency.

An explicit pair is

`a = 01000111001011`,

`b = 01001011100011`.

Both begin with `010`, end with `011`, and have exactly the same complete length-four-block multiset,

`{0001,0010,0011,0100,0101,0111,1000,1001,1011,1100,1110}`,

with every listed block occurring once. Hence, under the identity quantizer on the binary alphabet, they lie in one exact `m=3` Markov type in the sense of `VIS-099`.

Nevertheless their ordinary three-delay polygonal paths

`w_i=(x_i,x_(i+1),x_(i+2)) in R^3`

have different fourth signature levels. With the coordinate convention used in `VIS-097`, exact Chen-expansion gives

`[S^4(X_a)-S^4(X_b)]_(1,2,1,3) = -1`.

By `VIS-096`, the shared endpoints and complete oriented-edge inventory already force equality through signature degree three. Thus the difference is a genuine higher-order chronology effect.

At the same time, if

`A(z)=sum_(j=0)^13 a_(j+1) z^j`,

`B(z)=sum_(j=0)^13 b_(j+1) z^j`,

then

`A(z)A(z^(-1)) = B(z)B(z^(-1))`

as an exact Laurent-polynomial identity. Therefore

`|A(e^(it))| = |B(e^(it))|`

for every real `t`. Equivalently, the two words have the same complete aperiodic autocorrelation and every magnitude-only Fourier spectrum or periodogram is identical.

The ambiguity is nontrivial: the words are neither translates nor reflected translates of one another.

**Evidence/status:** `EXACT-DERIVED + INFORMATION-BOUNDARY + DECISIVE-NEGATIVE + CLASSICAL-PHASE-RETRIEVAL AMBIGUITY + NO-NOVELTY-CLAIM`.

This result does not establish a zeta-specific signal. It closes a natural candidate representation: **ordinary Fourier magnitude / power-spectrum views cannot serve as a generally sufficient replacement for the chronology information already known to survive the exact local-block quotient.**

## 1. The pair lies in one exact order-three Markov type

Reading consecutive length-four blocks from `a` gives

`0100,1000,0001,0011,0111,1110,1100,1001,0010,0101,1011`.

Reading them from `b` gives

`0100,1001,0010,0101,1011,0111,1110,1100,1000,0001,0011`.

The two lists are permutations of the same eleven distinct blocks. Their initial triple is `010`, and the common transition table therefore has count one on exactly

`0001,0010,0011,0100,0101,0111,1000,1001,1011,1100,1110`

and count zero on the remaining binary four-blocks.

This is precisely the data defining the exact third-order Markov type of `VIS-099`: the two words are alternative Eulerian assemblies of the same directed three-context edge multiset.

Because the final triple is also common (`011`), the corresponding three-delay paths have the same initial and final vertices. `VIS-096` then applies directly: all signature information through degree three is fixed by that oriented local-edge inventory.

## 2. Degree four distinguishes the assemblies exactly

For a piecewise-linear path with successive increments `d`, the segment signature is

`exp_tensor(d) = sum_(k>=0) d^(tensor k)/k!`,

and concatenation multiplies these tensor series by Chen's identity. Consequently the degree-`k` signature can be evaluated recursively, with exact rational arithmetic, by

`S_new^k = sum_(j=0)^k S_old^(k-j) tensor d^(tensor j)/j!`.

Applying this recurrence to the eleven three-delay increments of the displayed words gives

`[S^4(X_a)-S^4(X_b)]_(1,2,1,3) = -1`.

The difference has sixteen nonzero tensor coordinates, all equal to `+1` or `-1`; one coordinate is enough to certify inequality. Since degrees one through three are already equal by the exact local-block theorem, this is not lower-order leakage disguised by another basis.

The pair therefore supplies a second explicit witness, distinct from the cycle-swap pair of `VIS-097`, that the exact order-three local quotient can leave real degree-four assembly information.

## 3. A reciprocal-factor flip erases the distinction from every Fourier magnitude

The generating polynomials are

`A(z)=z+z^5+z^6+z^7+z^10+z^12+z^13`,

`B(z)=z+z^4+z^6+z^7+z^8+z^12+z^13`.

They factor as

`A(z)=z (z^3-z+1) Q(z)`,

`B(z)=z (z^3-z+1) Q*(z)`,

where

`Q(z)=z^9+z^8+z^7+z^6+z^2+z+1`,

`Q*(z)=z^9 Q(z^(-1))`

`     =z^9+z^8+z^7+z^3+z^2+z+1`.

For `|z|=1`, real coefficients give

`Q*(z)=z^9 conjugate(Q(z))`,

so `|Q*(z)|=|Q(z)|`. The remaining factors of `A` and `B` are identical, hence

`|A(z)|=|B(z)|` for every `|z|=1`.

Equivalently,

`A(z)A(z^(-1))=B(z)B(z^(-1))`.

The Laurent coefficients are the aperiodic autocorrelations

`r(k)=sum_j x_j x_(j+k)`.

For both words, for lags `k=0,...,13`, the exact autocorrelation vector is

`(7,3,2,2,2,3,3,2,1,1,0,1,1,0)`.

Thus this is not merely equality on one chosen FFT grid: the full continuous Fourier intensity on the unit circle is identical.

## 4. The ambiguity is not just global translation or reflection

With zero-based indices, the supports are

`S_a={1,5,6,7,10,12,13}`,

`S_b={1,4,6,7,8,12,13}`.

Both have minimum `1` and maximum `13`. Any translate mapping one finite support to the other must therefore have translation zero, but `S_a != S_b`.

Any reflected translate preserving the same extrema must be the reflection `j -> 14-j`. It sends `S_a` to

`{1,2,4,7,8,9,13}`,

which is also different from `S_b`.

The equality of Fourier magnitude is therefore a genuine one-dimensional phase-retrieval ambiguity produced by reversing only the factor `Q`, not by reversing or shifting the complete word.

## 5. Prior art and novelty assessment

Fourier-magnitude nonuniqueness in one dimension is classical phase-retrieval theory. M. H. Hayes, J. S. Lim, and A. V. Oppenheim, **Signal reconstruction from phase or magnitude**, *IEEE Transactions on Acoustics, Speech, and Signal Processing* 28:6 (1980), 672–680, DOI `10.1109/TASSP.1980.1163463`, studies conditions under which a finite sequence is or is not determined by Fourier phase or magnitude.

Robert Beinert and Gerlind Plonka, **Ambiguities in One-Dimensional Discrete Phase Retrieval from Fourier Magnitudes**, *Journal of Fourier Analysis and Applications* 21:6 (2015), 1169–1198, DOI `10.1007/s00041-015-9405-2`, gives a dedicated classification of trivial and nontrivial ambiguities for finitely supported one-dimensional signals. Dan Edidin, **The Geometry of Ambiguity in One-Dimensional Phase Retrieval**, *SIAM Journal on Applied Algebra and Geometry* 3:4 (2019), 644–660, DOI `10.1137/18M1230530`, studies the corresponding root-covering geometry.

Accordingly, no novelty is claimed for reciprocal-factor flips, Fourier phase retrieval, homometric/autocorrelation ambiguity, or the identity between Fourier intensity and autocorrelation.

The Mathia-specific content is the **intersection of that classical ambiguity with the exact local-block chronology boundary already isolated in this line**: the displayed pair lies in one exact order-three Markov type but carries different degree-four path-signature information. It gives an explicit information-loss certificate for a natural spectral visualization proposed at precisely the current frontier.

## Boundary and falsification

This finding concerns one explicit binary exact-Markov-type pair. It does **not** prove that:

- every order-three Markov type contains Fourier-homometric alternatives;
- Fourier phase, complex Fourier coefficients, bispectra, polyspectra, wavelets, short-time Fourier transforms, or other phase-sensitive/higher-order spectral representations lose the same information;
- degree-four path signature is universally superior to spectral methods;
- the surviving signature coordinate is arithmetic-specific;
- zeta zeros differ from a matched finite-size CUE ensemble under any phase-sensitive statistic;
- any Fourier or signature statistic yields an RH criterion.

The exact claim is falsified by any one of the following: unequal length-four transition tables for the displayed words; failure of the Laurent identity `A(z)A(z^(-1))=B(z)B(z^(-1))`; or equality of their stated fourth-signature coordinate under the same three-delay convention.

## Visual consequence

No canonical PNG is retained. A magnitude-spectrum rendering would place the two Fourier-intensity curves exactly on top of one another and therefore **hide** the distinction being certified. The factorization and autocorrelation identity are the more faithful representation of this negative result.

A future phase-sensitive visualization may still be useful, but it would be a new research question and is deliberately left outside this invocation.

## Research consequence

The accepted critical-strip multiscale clue asks for a materially different carrier after the exact local-block quotient and the collapse of most of the area-area channel. This finding rules out one tempting answer at the information level: **ordinary Fourier magnitude, power spectrum, and any statistic determined solely by the complete two-point autocorrelation cannot be treated as a generally sufficient nonlocal chronology carrier.**

Any future spectral continuation should state explicitly what information beyond Fourier magnitude/autocorrelation it preserves. Phase-sensitive or genuinely higher-order spectral constructions remain open, as do non-spectral carriers, but they require their own exact lower-information audit before source-specific testing.